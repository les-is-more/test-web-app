from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullName = Column(String)
    nickName = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullName='%s', nickName='%s')>" % (self.name,self.fullName,self.nickName)


ed_user = User(name='Lester')
print(ed_user)