from pydantic import BaseModel

class CreateEmailCommand(BaseModel):
    folder_id: int
    subject: str
    body: str