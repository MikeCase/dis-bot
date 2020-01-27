from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date

engine = create_engine('sqlite:///bot_db.db')
session = sessionmaker(bind=engine)()

Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    created_at = Column(Date)

    def __init__(self, user, email, password):

        self.user = user
        self.password = password
        self.email = email
        self.created_at = 'date_placeholder'

    def __repr__(self):
        return f'<User(name={self.user}, email={self.email}, password=*******, created_at={self.created_at})'

Base.metadata.create_all(engine)