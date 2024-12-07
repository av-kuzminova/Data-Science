from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.utils import hash_password

router = APIRouter()

@router.post("/")
def create_user(login: str, first_name: str, last_name: str, password: str, db: Session = Depends(SessionLocal)):
    hashed_password = hash_password(password)
    user = User(login=login, first_name=first_name, last_name=last_name, password_hash=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "login": user.login}

@router.get("/")
def search_users(login: str, db: Session = Depends(SessionLocal)):
    return db.query(User).filter(User.login == login).first()