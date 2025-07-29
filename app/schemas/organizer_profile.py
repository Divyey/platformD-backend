from pydantic import BaseModel
from typing import Optional

class OrganizerProfileBase(BaseModel):
    company_name: Optional[str]
    contact_info: Optional[str]
    ratings: Optional[float]
    reviews: Optional[str]
    social_links: Optional[str]

class OrganizerProfileOut(OrganizerProfileBase):
    user_id: int

    class Config:
        from_attributes = True
