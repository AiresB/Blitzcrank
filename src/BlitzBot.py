from discord.ext import commands

class BlitzBot(commands.Bot):

    async def on_ready(self):
            """
            type: event
            activate when the bot is connected and print in the console log
            """
            print("Bot connected")