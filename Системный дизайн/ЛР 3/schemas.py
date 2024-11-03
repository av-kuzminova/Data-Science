from pydantic import BaseModel

class User(BaseModel):
    username: str
    full_name: str
    email: str

    class Config:
        orm_mode = True

class UserCreate(User):
    password: str
