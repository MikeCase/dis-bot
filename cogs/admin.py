import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, module):
        """ Reload module """
        member = await ctx.author.create_dm()
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await member.send(f'{e.__class__.__name__}: {e}')
        else:
            await member.send('\N{OK HAND SIGN}')

    @reload.error
    async def reload_error(self, ctx, error):
        member = await ctx.author.create_dm()
        await member.send('I don\'t think you want to be trying that.')

def setup(bot):
    bot.add_cog(Admin(bot))