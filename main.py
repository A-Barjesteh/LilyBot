import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print ("Hello! I exist")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! I exist")

@bot.command()
async def add(ctx,x,y):
    result = int(x) + int(y)
    await ctx.send(f"{x} + {y} = {result}")

bot.run(BOT_TOKEN)