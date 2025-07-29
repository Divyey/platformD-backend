from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time, datetime
from enum import Enum

class EventMode(str, Enum):
    online = "online"
    offline = "offline"
    both = "both"

class EventBase(BaseModel):
    title: str
    description: str
    event_date: date
    event_time: Optional[time]
    location: str
    mode: EventMode
    category: str
    subcategories: Optional[List[str]] = None
    banner_image_url: Optional[str] = None  # main image
    image_urls: Optional[List[str]] = None  # multiple images (not stored yet)
    community_id: Optional[int] = None

class EventCreate(EventBase):
    pass

class EventOut(EventBase):
    id: int
    organizer_id: int
    organizer_rating: Optional[float]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
