#!/usr/bin/env python3

from multiprocessing import Process
import logging
import os
import subprocess
import http.server as web

import discord

bot = discord.Bot()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@bot.slash_command()
async def yt(ctx, query: str):
    cmd = subprocess.run(["ytgo", "-d", query], stdout=subprocess.PIPE, text=True)
    await ctx.respond(cmd.stdout)


def bot_server():
    logger.info("Starting Bot...")
    bot.run(os.getenv("BOT_TOKEN"))
    logger.info("Bot Stopped...")


def web_server(server_class=web.HTTPServer, handler_class=web.BaseHTTPRequestHandler):
    server_address = ("", 10000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def persistent_runner(f):
    while True:
        try:
            f()
        except KeyboardInterrupt:
            logger.warning("Received SIGINT. Exiting function run.")
            break
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    p1 = Process(target=persistent_runner, args=(bot_server,))
    p2 = Process(target=persistent_runner, args=(web_server,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
