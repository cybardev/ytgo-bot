#!/usr/bin/env python3

import asyncio
import contextlib
import os
import subprocess

import discord

from aiohttp import web


async def _web_handler(request):
    """
    We use this because Render requires free web services to
    bind to a port regardless if it's used in the application
    """
    return web.Response(
        text="Bot has been awakened from sleep. You can use it again now."
    )


async def _bot_server(bot):
    async with bot:
        await bot.start(os.getenv("BOT_TOKEN"))


async def _run_bot(_app, bot):
    task = asyncio.create_task(_bot_server(bot))

    yield

    task.cancel()
    with contextlib.suppress(asyncio.CancelledError):
        await task  # Ensure any exceptions etc. are raised.


bot = discord.Bot()


@bot.slash_command(
    description="Get the first video URL from a YouTube search",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
@discord.option("query", description="What to search")
@discord.option("num", description="Which search result to use")
@discord.option("embed", description="Whether to show video embed")
async def yt(ctx, query: str, num: int = 1, embed: bool = True):
    await ctx.defer()
    cmd = subprocess.run(
        ["ytgo", "-d", query, "-n", str(num)], stdout=subprocess.PIPE, text=True
    )
    await ctx.respond(cmd.stdout if embed else f"<{cmd.stdout.strip()}>")


def main(bot):
    app = web.Application()
    app.add_routes([web.get("/", _web_handler)])
    app.cleanup_ctx.append(lambda _app: _run_bot(_app, bot))
    web.run_app(app, port=10000)


if __name__ == "__main__":
    main(bot)
