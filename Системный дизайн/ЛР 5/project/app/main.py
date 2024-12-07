from fastapi import FastAPI
from app.routes import users, folders, messages

app = FastAPI()

# Подключение маршрутов
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(folders.router, prefix="/folders", tags=["Folders"])
app.include_router(messages.router, prefix="/messages", tags=["Messages"])