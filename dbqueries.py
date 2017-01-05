from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User
# choosing database to work
engine = create_engine('sqlite:///database.db')
# connection betweens classes and tables
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

def getUsers():
	users = session.query(User).all()
	return users

def insertUser(name):
	user = User(name=name)
	session.add(user)
	session.commit()

