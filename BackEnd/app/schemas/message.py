from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    event: str
    content: str
    user_id: Optional[str] = None


class ResponseMessage(BaseModel):
    status: int
    content: str
