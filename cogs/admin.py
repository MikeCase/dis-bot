import discord
from discord.ext import commands
from datetime import datetime
from utils.db import Session, User, Promote
from sqlalchemy import and_


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

    @commands.command()
    @commands.is_owner()
    async def add_user(self, ctx, username, password, email, greeting='Hey ya\'ll'):
        session = Session()
        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.greeting = greeting
        user.created_at = datetime.now()

        session.add(user)

        try:
            session.commit()
            await ctx.send(f'Created user: {username}!')
        except:
            await ctx.send('That didn\'t work')

        session.close()

    @commands.command()
    @commands.is_owner()
    async def rm_user(self, ctx, username, email):
        session = Session()
        user = session.query(User).filter_by(username=username).filter_by(email=email).first()
        await ctx.send(f"Removing {user.username} from the database")
        session.delete(user)
        session.commit()
        session.close()

def setup(bot):
    bot.add_cog(Admin(bot))