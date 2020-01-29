import re
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class Shopper(commands.Cog):

    """ Online price search with the bot. 
    search for prices on what you want. """

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def amzn(self, ctx, *, search):
        """Search Amazon"""
        # Strip whitespace and insert + signs 
        search_term = search.replace(' ', '+')

        # set headers so amazon will crumble at our mighty...uhm... ok the thought ended there.. anyways.. 
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }
        # @todo - fix this. Returns empty list
        # sure it has to do with the xpath 
        print(f'https://www.amazon.com/s?k={search_term}')
        r = requests.get(f'https://www.amazon.com/s?k={search_term}', headers=headers)
        # xpath = '//*[@id="search"]*/h2/a'
        soup = BeautifulSoup(r.text, 'html.parser')
        # links = r.status_code
        print(soup)
        # print(links.find('a'))
        #await ctx.send(links)

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