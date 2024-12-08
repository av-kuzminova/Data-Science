from fastapi import FastAPI
from src.kafka_producer import publish_event
from src.commands import CreateEmailCommand
from src.queries import GetEmailsQuery

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Email Service API"}

@app.post("/emails/")
def create_email(command: CreateEmailCommand):
    # Публикация события в Kafka
    publish_event("emails", command.dict())
    return {"status": "Email creation event published"}

@app.get("/emails/")
def get_emails(query: GetEmailsQuery):
    # Здесь предполагается, что данные извлекаются из базы данных
    return {"emails": f"Emails for folder {query.folder_id}"}