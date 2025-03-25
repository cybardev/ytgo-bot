#!/usr/bin/env python3

import os
import subprocess

import discord

bot = discord.Bot()


@bot.slash_command(
    description="Get the first video URL from a YouTube search",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
@discord.option("query", description="What to search")
@discord.option("embed", description="Whether to show video embed")
async def yt(ctx, query: str, embed: bool = True):
    cmd = subprocess.run(["ytgo", "-d", query], stdout=subprocess.PIPE, text=True)
    await ctx.respond(cmd.stdout)


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
