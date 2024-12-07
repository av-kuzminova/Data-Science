from fastapi import APIRouter
from app.database import mongo_db
from datetime import datetime

router = APIRouter()

@router.post("/")
def create_message(folder_id: str, sender: str, recipient: str, subject: str, body: str):
    message = {
        "folder_id": folder_id,
        "sender": sender,
        "recipient": recipient,
        "subject": subject,
        "body": body,
        "timestamp": datetime.utcnow().isoformat()
    }
    mongo_db.messages.insert_one(message)
    return {"message": "Message created successfully"}