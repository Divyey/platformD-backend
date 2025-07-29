from __future__ import annotations

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    contact_number: Optional[str] = None
    bio: Optional[str] = None
    interests: Optional[List[str]] = None  # Changed to List[str]
    avatar_url: Optional[str] = None
    locale: Optional[str] = "en"

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    roles: Optional[str]
    is_active: bool
    is_verified: bool
    created_at: Optional[datetime]
    last_login: Optional[datetime]

    communities_created: Optional[List["CommunityOut"]] = None
    communities: Optional[List["CommunityOut"]] = None

    class Config:
        from_attributes = True

from app.schemas.community import CommunityOut
UserOut.update_forward_refs()
