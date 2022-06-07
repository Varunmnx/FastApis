from tokenize import String
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.sql.expression import null
from .database import Base


class Post(Base):
    __table__ ="posts"
    id = Column(Integer,primary_key= True,nullable=False)
    name = Column(String,nullable =False)
    content = Column(String,nullable = False)
    publish
