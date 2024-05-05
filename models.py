# models.py

from sqlalchemy import Column, Integer, String
from database import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String(64), unique=True)
    hashed_password= Column(String)




class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Specify the length (e.g., 255 characters)
    description = Column(String(255), index=True)
    price = Column(Integer)
