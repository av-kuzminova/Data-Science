from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
import redis

# PostgreSQL
DATABASE_URL = "postgresql://user:password@db/app"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# MongoDB
MONGO_URL = "mongodb://mongo:27017"
mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["email_service"]

# Redis
REDIS_URL = "redis://redis:6379"
redis_client = redis.StrictRedis.from_url(REDIS_URL)