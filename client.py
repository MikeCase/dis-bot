import os, traceback, sys
import discord
from discord.ext import commands
from discord.ext.commands import Cog
from config import BOT_TOKEN

bot = commands.Bot(command_prefix='!')
bot_extensions = [
    'cogs.admin',
    'cogs.greetings',
]

@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.NotOwner):
        member = await ctx.author.create_dm()
        await member.send("Naughty, naughty.")
    else:
        if hasattr(ctx.command, 'on_error'): # does ctx.command have an on_error attribute? 
            return

        cog = ctx.cog # ctx.cog = cog 
        if cog: # if cog is valid continue
            if Cog._get_overridden_method(cog.cog_command_error) is not None: # cog.cog_command_error is the overridden method. 
                return

    #print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    #traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

async def load_cogs(ctx):
    for cog in ctx:
        print(f'Loading extension {cog}')
        bot.load_extension(cog)

@bot.event
async def on_ready():
    await load_cogs(bot_extensions)
    print(f'Loaded and ready.')

bot.run(f'{BOT_TOKEN}')
