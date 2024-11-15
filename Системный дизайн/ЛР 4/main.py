# main.py

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from jose import JWTError, jwt
from passlib.context import CryptContext
from pymongo import MongoClient
from models import Base, User, Item, Order
import os

# Настройки
SECRET_KEY = "secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# URL базы данных PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/my_service")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# URL базы данных MongoDB
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://root:example@localhost:27017")
mongo_client = MongoClient(MONGODB_URL)
mongo_db = mongo_client.my_service_db

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Модель для создания заказа
class OrderCreate(BaseModel):
    order_number: int
    description: str
    amount: float

# Эндпоинты для MongoDB
@app.post("/orders")
def create_order(order: OrderCreate):
    if mongo_db.orders.find_one({"order_number": order.order_number}):
        raise HTTPException(status_code=400, detail="Order with this number already exists")
    mongo_db.orders.insert_one(order.dict())
    return {"status": "Order created successfully"}

@app.get("/orders/{order_number}", response_model=Order)
def get_order(order_number: int):
    order = mongo_db.orders.find_one({"order_number": order_number})
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return Order(**order)

# Остальные эндпоинты для PostgreSQL остаются без изменений
# ...
