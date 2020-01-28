import discord
from discord.ext import commands

class Shopper(commands.Cog):

    """ Online price search with the bot. 
    search for prices on what you want. """

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def amzn(self, ctx, *, search):
        pass

    @commands.command()
    async def ebay(self, ctx, *, search):
        pass

    @commands.command()
    async def nweg(self, ctx, *, search):
        pass

    @commands.command()
    async def gogl(self, ctx, *, search):
        pass
