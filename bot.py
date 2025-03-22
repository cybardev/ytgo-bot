#!/usr/bin/env python3

import subprocess

import discord

from utils import main

bot = discord.Bot()


@bot.slash_command(description="Get the first video URL from a YouTube search")
@discord.option("query", description="What to search")
async def yt(ctx, query: str):
    cmd = subprocess.run(["ytgo", "-d", query], stdout=subprocess.PIPE, text=True)
    await ctx.respond(cmd.stdout)


def serve_bot(token):
    bot.run(token)


if __name__ == "__main__":
    main(serve_bot)
