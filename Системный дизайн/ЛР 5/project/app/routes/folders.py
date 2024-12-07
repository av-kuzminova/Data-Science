import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, redis_client
from app.models import Folder

router = APIRouter()

@router.get("/{folder_id}")
def get_folder(folder_id: int, db: Session = Depends(SessionLocal)):
    cached_folder = redis_client.get(f"folder:{folder_id}")
    if cached_folder:
        return {"source": "cache", "data": json.loads(cached_folder)}
    
    folder = db.query(Folder).filter(Folder.id == folder_id).first()
    if not folder:
        return {"error": "Folder not found"}
    
    folder_data = {"id": folder.id, "user_id": folder.user_id, "name": folder.name}
    redis_client.setex(f"folder:{folder_id}", 3600, json.dumps(folder_data))
    return {"source": "database", "data": folder_data}