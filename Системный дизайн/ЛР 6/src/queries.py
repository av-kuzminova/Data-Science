from pydantic import BaseModel

class GetEmailsQuery(BaseModel):
    folder_id: int