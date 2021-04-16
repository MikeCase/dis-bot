import discord
from discord.ext import commands
from datetime import datetime
from utils.db import Session, User, Promote
from sqlalchemy import and_
from config import BOT_OWNER

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.owner = BOT_OWNER
        self._last_result = None
        self.sessions = set()


    @commands.command()
    @commands.is_owner()
    async def kick(self, ctx, username, *args):
        
        pass


    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, module):
        """ Reload module 
        
            Reloads the specified module or all modules if none defined. 
            
            [prefix]reload {module}
            [prefix]reload 
            
        """
        # make sure the response is always sent as a direct message to the user
        member = await ctx.author.create_dm()

        try:
            print(f'Reloading {module} module...')
            self.bot.reload_extension(f'cogs.{module}')
        except commands.ExtensionError as e:
            await member.send(f'{e.__class__.__name__}: {e}')
        else:
            print(f'Module {module} reloaded successfully... ')
            await member.send('\N{OK HAND SIGN}') # direct message 

    @reload.error
    async def reload_error(self, ctx, error):
        member = await ctx.author.create_dm()
        await member.send('I don\'t think you want to be trying that.')

    @commands.command()
    @commands.is_owner()
    async def add_user(self, ctx, username, password, email, greeting=f'Hey!'):
        """ Add a user to the database 

            [prefix]add_user {username} {password} {email} [optional]{greeting}[/optional]
        """
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
        except:
            await ctx.send('That didn\'t work')
        else:
            await ctx.send(f'Created user: {username}!')

        session.close()

    @commands.command()
    @commands.is_owner()
    async def rm_user(self, ctx, username, email):
        """ Remove user

            Removes a user in the database
            [prefix]rm_user {username} {user email}
        """

        session = Session()
        user = session.query(User).filter_by(username=username).filter_by(email=email).first()
        print(f"Removing {user.username} from the database")
        await ctx.send(f"Removing {user.username} from the database")
        session.delete(user)
        try:
            session.commit()
        except:
            await ctx.send("That didn't work.")
        else:
            print(f'{user.username} has been removed.')
            await ctx.send(f'{user.username} has been removed.')
        session.close()

def setup(bot):
    bot.add_cog(Admin(bot))