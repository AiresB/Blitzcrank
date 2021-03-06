import discord
import os

import src.front.commands.token as token

from src.back.riot import get_ranking
from src.back.riot_api import RiotAPI
from src.back.player import Player
from src.back.database import Database

class Base(discord.ext.commands.Cog, name='Base functions'):

    def __init__(self, bot):
        self.bot = bot
        self.list = []
        self.db = Database(os.getenv("DATABASE_URL"))
        for l in self.db.get_players():
            self._load(l[1])

    def _load(self, pseudo):
        status, res = RiotAPI().get_tft_player_by_pseudo(pseudo, token.RIOT_TOKEN)

        if status != 200:
            print(res["status"]["message"])
            return
        elif self._get_player_from_list(res["name"]) != None:
            print(f"Error: {pseudo} already registered")
            return

        new_player = Player(res)
        self.list.append(new_player)

    @discord.ext.commands.command(name="add")
    async def add(self, ctx,*, arg):
        """
        type: command
        create a new player from the pseudo
        Args:
            ctx : [context]
            arg (str): [pseudo of the player created]
        """
        status, res = RiotAPI().get_tft_player_by_pseudo(arg, token.RIOT_TOKEN)

        if status != 200:
            await ctx.message.channel.send(res["status"]["message"])
            return
        elif self._get_player_from_list(res["name"]) != None:
            await ctx.message.channel.send(f"Error: {arg} already registered")
            return

        new_player = Player(res)
        self.list.append(new_player)
        self.db.add_player(new_player.pseudo)
        await ctx.message.channel.send(new_player.pseudo + " added")

    def _get_player_from_list(self, pseudo):
        for player in self.list:
            if player.pseudo == pseudo:
                return player
        return None

    @discord.ext.commands.command(name="remove")
    async def rm(self, ctx, *,pseudo):
        """
        type: command
        remove the player from the pseudo
        Args:
            ctx : [context]
            pseudo (str): [pseudo of the player created]
        """
        player = self._get_player_from_list(pseudo)
        if player == None:
            await ctx.message.channel.send(pseudo + " is not registered")

        else:
            self.list.remove(player)
            await ctx.message.channel.send(player.pseudo + " removed")
            self.db.delete_player(player.pseudo)
            del player

    @discord.ext.commands.command(name="ranking")
    async def ranking(self, ctx):
        """
        type: command
        give the ranking of the players registered
        Args:
            ctx : [context]
        """
        rank = get_ranking(self.list, token.RIOT_TOKEN)
        res = "Ranking:\n"
        for r in rank:
            res += r[0] + "\n"
        await ctx.message.channel.send(res)

    @discord.ext.commands.command(name="list")
    async def lst(self, ctx):
        res = "Registered players:\n"
        for players in self.list:
            res += players.pseudo
            res += "\n"
        await ctx.message.channel.send(res)
