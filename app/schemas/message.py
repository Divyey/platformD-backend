from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MessageBase(BaseModel):
    content: str
    recipient_id: Optional[int] = None
    chat_id: Optional[int] = None

class MessageCreate(MessageBase):
    sender_id: int

class MessageOut(MessageBase):
    id: int
    timestamp: datetime
    read_status: bool
    notification_type: str
    notification_on: bool
    silent: bool

    class Config:
        from_attributes = True
