import os
import discord
from discord.ext import commands
from config import BOT_TOKEN

bot = commands.Bot(command_prefix='!')
bot_extensions = [
    'cogs.admin',
    'cogs.greetings',
]
async def load_cogs(ctx):
    for cog in ctx:
        print(f'Loading extension {cog}')
        bot.load_extension(cog)

@commands.Cog.listener()
async def on_ready():
    load_cogs(bot_extensions)
    print(f'Loaded and ready.')

bot.run(f'{BOT_TOKEN}')
