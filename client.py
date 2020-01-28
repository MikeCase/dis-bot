import os, traceback, sys
import discord
from discord.ext import commands
from config import BOT_TOKEN

bot = commands.Bot(command_prefix='!')
bot_extensions = [
    'cogs.admin',
    'cogs.greetings',
    'cogs.promote',
    'cogs.shop',
]

async def load_cogs(ctx):
    for cog in ctx:
        print(f'Loading extension {cog}')
        bot.load_extension(cog)

@bot.event
async def on_ready():
    await load_cogs(bot_extensions)
    print(f'Loaded and ready.')

bot.run(f'{BOT_TOKEN}')
