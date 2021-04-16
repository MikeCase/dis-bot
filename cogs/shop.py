import re
import random
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from ebaysdk.finding import Connection as Finding
import pprint

class Shopper(commands.Cog):

    """ Online price search with the bot. 
    search for prices on what you want. """

    def __init__(self,bot):
        self.bot = bot
        self.app = 'MichaelC-DiscordB-PRD-bcbc14c9f-076e7c02'

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
        api = Finding(appid=self.app, config_file=None)
        count = 3
        data = {
            'keywords': search,
            'paginationInput': {
                'entriesPerPage': f'{count}',
                'pageNumber': '1',
                }
            }
        resp = api.execute('findItemsAdvanced', data=data)
    
        # pprint.pprint(resp.dict())
        # results = resp
        # print(dir(resp.reply))
        if resp.reply.ack == 'Success':
            # member = await ctx.channel
            item_url = resp.reply.itemSearchURL
            items = resp.reply.searchResult.item
            embed = discord.Embed(title="Search results", url=item_url, color=discord.Colour.dark_teal())
            embed.add_field(name='Requested By', value=ctx.author.name)
            for i in items:
                # print(dir(i))
                embed.set_thumbnail(url=i.galleryURL)
                # embed.add_field(name='image', value=i.galleryURL, inline=False)
                embed.add_field(name='Title', value=f'[{i.title}]({i.viewItemURL})', inline=False)
                embed.add_field(name='Price', value=i.sellingStatus.currentPrice.value, inline=False)

            if command.is_owner():
            embed.set_footer(text='Your results Sire.')

                
            await ctx.send(embed=embed)



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