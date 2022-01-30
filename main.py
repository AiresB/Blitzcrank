import os

from discord.ext import commands
from dotenv import load_dotenv
from riot import get_rank, get_list

load_dotenv(dotenv_path="config")

RIOT_TOKEN = os.getenv("RIOT_TOKEN")
DISCORD_TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="!")

lst = []

@bot.event
async def on_ready():
    """
    type: event
    activate when the bot is connected and print in the console log
    """
    print("Bot connected")

@bot.command(name="add")
async def add(ctx, pseudo: str):
    """
    type: command
    create a new player from the pseudo
    Args:
        ctx : [context]
        pseudo (str): [pseudo of the player created]
    """
    lst.append(pseudo)
    await ctx.message.channel.send(pseudo + " added")

@bot.command(name="remove")
async def rm(ctx, pseudo: str):
    """
    type: command
    remove the player from the pseudo
    Args:
        ctx : [context]
        pseudo (str): [pseudo of the player created]
    """
    lst.remove(pseudo)
    await ctx.message.channel.send(pseudo + " removed")

@bot.command(name="ranking")
async def ranking(ctx):
    """
    type: command
    give the ranking of the players registered
    Args:
        ctx : [context]
    """
    res = get_list(lst, RIOT_TOKEN)
    for r in res:
        await ctx.message.channel.send(r[0])

@bot.command(name="token")
async def token(ctx, token: str):
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

bot.run(DISCORD_TOKEN)