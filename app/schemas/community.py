from __future__ import annotations

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CommunityBase(BaseModel):
    name: str
    description: Optional[str] = None

class CommunityCreate(CommunityBase):
    pass

class CommunityUpdate(CommunityBase):
    pass

class CommunityOut(CommunityBase):
    id: int
    creator_id: int
    created_at: datetime
    members: Optional[List[int]] = None  # Can be user IDs or a schema of members if more detailed
    class Config:
        from_attributes = True
        # orm_mode = True  # Correct config for ORM models

# Forward references for UserOut
from app.schemas.user import UserOut
CommunityOut.update_forward_refs()
