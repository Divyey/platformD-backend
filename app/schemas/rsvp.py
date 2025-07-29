from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional

class RSVPStatus(str, Enum):
    going = "going"
    interested = "interested"
    declined = "declined"

class RSVPBase(BaseModel):
    status: RSVPStatus

class RSVPCreate(RSVPBase):
    user_id: int
    event_id: int

class RSVPOut(RSVPBase):
    id: int
    user_id: int
    event_id: int
    created_at: datetime

    class Config:
        from_attributes = True
