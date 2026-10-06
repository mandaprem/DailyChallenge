from sqlalchemy import Column,Integer,String
from src.utils.db import Base

class userModel(Base):
    __tablename__ = "User"

    id = Column (Integer,unique=True,primary_key=True,autoincrement=True)
    user_name = Column (String,unique=True,primary_key=True)
    email = Column (String,unique=True ,nullable=False)
    password_hashed = Column(String ,nullable=False)
    role = Column(String)