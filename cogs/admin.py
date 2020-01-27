import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    @commands.command(name='reload',pass_context=True)
    @commands.is_owner()
    async def reload(self, ctx, *, module):
        """ Reload module """
        member = await ctx.author.create_dm()
        # When a non owner trys to use this command it raises NotOwner 
        # What I want to do is push that error to the user to let them know.
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await member.send(f'{e.__class__.__name__}: {e}')
        else:
            await member.send('\N{OK HAND SIGN}')

def setup(bot):
    bot.add_cog(Admin(bot))