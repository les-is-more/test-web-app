from db import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'user_info'
    idx = Column(Integer,primary_key=True)
    firstName = Column(String(120), unique= True )

    def __init__(self, idx=None, firstName=None):
        self.idx = idx
        self.firstName = firstName

    # This __repr__ attrib is optional

