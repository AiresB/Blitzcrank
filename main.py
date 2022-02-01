#!/usr/bin/env python3
import os
import discord
from dotenv import load_dotenv

from src.BlitzBot import BlitzBot
from src.front.commands.token import Token
from src.front.commands.base import Base

load_dotenv(dotenv_path="config")

def main():
    token = os.getenv("BOT_TOKEN")

    intents = discord.Intents.default()
    intents.members = True

    bot = BlitzBot(
        command_prefix='!',
        intents=intents
    )

    bot.add_cog(Token(bot))
    bot.add_cog(Base(bot))

    bot.run(token)


if __name__ == '__main__':
    main()