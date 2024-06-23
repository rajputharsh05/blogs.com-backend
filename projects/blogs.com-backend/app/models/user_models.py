from sqlalchemy import create_engine ,Column , Integer ,String , DATETIME ,ForeignKey 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , relationship


Base = declarative_base()

class User(Base):

    __tablename__ = "User"

    id = Column(Integer , primary_key = True)
    name = Column(String(255) ,nullable=False)
    email = Column(String(255) , nullable=False,unique=True)
    password = Column(String(255) , nullable=False)