import os
import discord

global RIOT_TOKEN

class Token(discord.ext.commands.Cog, name='Token module'):

    def __init__(self, bot):
        global RIOT_TOKEN
        RIOT_TOKEN = os.getenv("RIOT_TOKEN")
        self.bot = bot


    @discord.ext.commands.command(name="token")
    async def token(self, ctx, token: str):
        """
        type: command
        change the riot token
        Args:
            ctx : [context]
            token (str): [riot api token]
        """
        global RIOT_TOKEN
        RIOT_TOKEN = token
        async for m in ctx.message.channel.history(limit=1):
            await m.delete()
