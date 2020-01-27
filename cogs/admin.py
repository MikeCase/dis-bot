import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, *, module):
        """ Reload module """
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        except commands.CheckFailure as e: 
            userMsg = await ctx.author.create_dm()
            await userMsg.send(f'{e}')
        else:
            await ctx.send('\N{OK HAND SIGN}')

def setup(bot):
    bot.add_cog(Admin(bot))