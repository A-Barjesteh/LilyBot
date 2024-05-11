import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    channel = bot.get_channel(1238894523195592744)
    await channel.send("Hello! I exist")

@bot.command()
async def add(ctx,x,y):
    result = int(x) + int(y)
    await ctx.send(f"{x} + {y} = {result}")

bot.run(BOT_TOKEN)
