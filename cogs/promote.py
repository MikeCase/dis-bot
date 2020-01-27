import discord
from discord.ext import commands


class Promote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def promote(self, ctx):
        member = ctx.author
        embed=discord.Embed(title='GitHub', url='https://www.github.com/MikeCase', description=f'GitHub Promotion for {member.mention}', color=0xff0000)
        embed.add_field(name='Website', value='http://www.mikecase.us', inline=False)
        embed.add_field(name='github url', value='http://www.github.com/MikeCase', inline=False)
        embed.set_footer(text='Check it out!')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Promote(bot))