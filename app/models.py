# from typing import Collection
# from email.policy import default
from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text


class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    Title=Column(String(255),nullable=False,unique=True)
    Content=Column(String(255),nullable=False)
    Published = Column(Boolean,server_default="TRUE")


    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"