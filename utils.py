import asyncio
import contextlib
import os

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


def main(bot):
    app = web.Application()
    app.add_routes([web.get("/", _web_handler)])
    app.cleanup_ctx.append(lambda _app: _run_bot(_app, bot))
    web.run_app(app, port=10000)
