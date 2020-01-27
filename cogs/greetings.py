import discord

from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ID = 670762221210697728
        self._last_member = None

    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hey {ctx.author.mention}!')

    @commands.command()
    async def users(self, ctx):
        memCount = ctx.guild.member_count.real
        await ctx.send(f'There are currently {memCount} users.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if str(channel) == "general":
                await channel.send(f'Welcome to the server {member.mention}')

def setup(bot):
    bot.add_cog(Greetings(bot))