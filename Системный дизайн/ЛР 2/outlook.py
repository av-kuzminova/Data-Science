from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta

# JWT
SECRET_KEY = "your_secret_key"  # Замените на ваш секретный ключ
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Мастер-пользователь
MASTER_USER = {
    "username": "admin",
    "password": "secret"
}

# Модель данных в памяти
users_db = {}
folders_db = {}
messages_db = {}

# Настройки для работы с паролями
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Настройки для OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

### Утилиты
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in users_db:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return users_db[username]
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

### Модели данных
class User(BaseModel):
    username: str
    full_name: str
    email: str

class UserCreate(User):
    password: str

class Folder(BaseModel):
    name: str

class Message(BaseModel):
    subject: str
    content: str
    sender: str
    recipient: str

class Token(BaseModel):
    access_token: str
    token_type: str

### Инициализация мастер-пользователя
users_db[MASTER_USER["username"]] = {
    "username": MASTER_USER["username"],
    "full_name": "Master Admin",
    "email": "admin@example.com",
    "hashed_password": get_password_hash(MASTER_USER["password"]),
}

### API Endpoints
# Создание нового пользователя
@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    users_db[user.username] = {
        "username": user.username,
        "full_name": user.full_name,
        "email": user.email,
        "hashed_password": hashed_password,
    }
    return users_db[user.username]

# Поиск пользователя по логину
@app.get("/users/{username}", response_model=User)
async def get_user_by_username(username: str):
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Поиск пользователя по маске имя и фамилии
@app.get("/users/search/")
async def search_user_by_name(full_name: str):
    result = [user for user in users_db.values() if full_name.lower() in user["full_name"].lower()]
    if not result:
        raise HTTPException(status_code=404, detail="No users found")
    return result

# Создание новой почтовой папки
@app.post("/folders/")
async def create_folder(folder: Folder, user: User = Depends(get_current_user)):
    if folder.name in folders_db:
        raise HTTPException(status_code=400, detail="Folder already exists")
    folders_db[folder.name] = []
    return {"message": "Folder created"}

# Получение перечня всех папок
@app.get("/folders/")
async def get_all_folders(user: User = Depends(get_current_user)):
    return list(folders_db.keys())

# Создание нового письма в папке
@app.post("/folders/{folder_name}/messages/")
async def create_message(folder_name: str, message: Message, user: User = Depends(get_current_user)):
    if folder_name not in folders_db:
        raise HTTPException(status_code=404, detail="Folder not found")
    message_data = message.dict()
    message_data["created_at"] = datetime.utcnow()
    folders_db[folder_name].append(message_data)
    return {"message": "Message created"}

# Получение всех писем в папке
@app.get("/folders/{folder_name}/messages/")
async def get_messages_in_folder(folder_name: str, user: User = Depends(get_current_user)):
    if folder_name not in folders_db:
        raise HTTPException(status_code=404, detail="Folder not found")
    return folders_db[folder_name]

# Аутентификация и получение токена
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}
