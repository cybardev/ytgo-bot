#!/usr/bin/env python3

import os
import discord


# This bot requires the 'message_content' intent.
class BotClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        # don't respond to own (bot) msgs
        if message.author == self.user:
            return

        if message.content.startswith("!yt"):
            response = "<PLACEHOLDER>"
            # TODO: get search query from msg
            # TODO: call ytgo with search query
            # TODO: send URL returned by ytgo
            await message.channel.send(response)


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    client = BotClient(intents=intents)
    client.run(os.getenv("BOT_TOKEN"))
