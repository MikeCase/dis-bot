from sqlalchemy import create_engine, Column, String, Integer, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///bot_db.db', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    """User Model"""
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)
    password = Column('password', String)
    email = Column('email', String)
    greeting = Column('greeting', String)
    created_at = Column('created_at', Date)

    def __init__(self, user="", password="", email="", greeting="", date=""):

        self.user = user
        self.password = password
        self.email = email
        self.greeting = greeting
        self.created_at = date

    def __repr__(self):
        return f'<User(username="{self.user}", email="{self.email}", greeting="{self.greeting}" password="*******", created_at="{self.created_at}")'
        
class Promote(Base):
    """Promote Model"""
    __tablename__ = 'promotes'

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    website = Column('website', String(120))
    github = Column('github', String(50))
    twitch = Column('twitch', String(50))
    bio = Column('bio', Text())

    def __init__(self, website, github, twitch, bio):
        self.website = website
        self.github = github
        self.twitch = twitch
        self.bio = bio

    def __repr__(self):
        return f'<Promote(user_id="{self.user_id}", website="{self.website}", twitch="{self.twitch}", bio="{self.bio}")'


Base.metadata.create_all(engine)