import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')
channel_id = os.getenv('CHANNEL_ID')

prefix = "!"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
  channel = bot.get_channel(int(channel_id))
  await channel.send('I am now running!')

@bot.command()
async def info(ctx):
  roles = list()
  for r in ctx.guild.roles:
    roles.append(r.name)
  await ctx.send(roles)

def main() -> None:
  bot.run(token)

if __name__ == '__main__':
  main()
