# from typing import Collection
# from email.policy import default
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import  String,Boolean,Integer,Column
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    Title=Column(String(255),nullable=False,unique=True)
    Content=Column(String(255),nullable=False)
    Published = Column(Boolean,server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"