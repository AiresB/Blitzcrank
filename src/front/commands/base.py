import discord

import src.front.commands.token as token

from src.back.riot import get_list
from src.back.player import Player

class Base(discord.ext.commands.Cog, name='Base functions'):

    def __init__(self, bot):
        self.bot = bot
        self.list = []

    @discord.ext.commands.command(name="add")
    async def add(self, ctx,*, arg):
        """
        type: command
        create a new player from the pseudo
        Args:
            ctx : [context]
            arg (str): [pseudo of the player created]
        """
        self.list.append(arg)
        await ctx.message.channel.send(arg + " added")

    @discord.ext.commands.command(name="remove")
    async def rm(self, ctx, pseudo: str):
        """
        type: command
        remove the player from the pseudo
        Args:
            ctx : [context]
            pseudo (str): [pseudo of the player created]
        """
        self.list.remove(pseudo)
        await ctx.message.channel.send(pseudo + " removed")

    @discord.ext.commands.command(name="ranking")
    async def ranking(self, ctx):
        """
        type: command
        give the ranking of the players registered
        Args:
            ctx : [context]
        """
        res = get_list(self.list, token.RIOT_TOKEN)
        for r in res:
            await ctx.message.channel.send(r[0])

    @discord.ext.commands.command(name="list")
    async def lst(self, ctx):
        await ctx.message.channel.send(self.list)
