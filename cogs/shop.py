import discord
from discord.ext import commands
from requests_html import HTMLSession

class Shopper(commands.Cog):

    """ Online price search with the bot. 
    search for prices on what you want. """

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def amzn(self, ctx, *, search):
        """Search Amazon"""
        
        # @todo - fix this. Returns empty list
        # sure it has to do with the xpath 
        r_session = HTMLSession()
        
        r = r_session.get(f'https://www.amazon.com/s?k={search}')
        xpath = '//*[@id="search"]/div[1]/h2/a/@inner-html'
        links = r.html.xpath(xpath)
        print(links)
        await ctx.send(links)

    @commands.command()
    async def ebay(self, ctx, *, search):
        """ Search Ebay """
        pass

    @commands.command()
    async def nweg(self, ctx, *, search):
        """ Search Newegg """
        pass

    @commands.command()
    async def gogl(self, ctx, *, search):
        """ Search Google Shopping """
        pass

def setup(bot):
    bot.add_cog(Shopper(bot))