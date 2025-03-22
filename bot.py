#!/usr/bin/env python3

import os
import subprocess

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


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    client = BotClient(intents=intents)
    client.run(os.getenv("BOT_TOKEN"))
