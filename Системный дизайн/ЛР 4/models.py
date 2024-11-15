# models.py

from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field
from bson import ObjectId

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Numeric)

# Модель Pydantic для Order в MongoDB
class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    order_number: int
    description: str
    amount: float
