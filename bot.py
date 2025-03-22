#!/usr/bin/env python3

from multiprocessing import Process
import os
import subprocess
import http.server as web

import discord


# This bot requires the 'message_content' intent.
class BotClient(discord.Client):
    prefix = "!yt"

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        # don't respond to own (bot) msgs
        if message.author == self.user:
            return

        if message.content.startswith(self.prefix):
            query = message.content[len(self.prefix) :].strip()
            cmd = subprocess.run(
                ["ytgo", "-d", query], stdout=subprocess.PIPE, text=True
            )
            await message.channel.send(cmd.stdout)


def bot_server():
    intents = discord.Intents.default()
    intents.message_content = True

    client = BotClient(intents=intents)
    client.run(os.getenv("BOT_TOKEN"))


def web_server(server_class=web.HTTPServer, handler_class=web.BaseHTTPRequestHandler):
    server_address = ("", 10000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    p1 = Process(target=bot_server)
    p2 = Process(target=web_server)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
