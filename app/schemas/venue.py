from pydantic import BaseModel
from typing import Optional

class VenueBase(BaseModel):
    name: str
    address: str
    city: str
    country: str
    zip: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    features: Optional[str]
    google_place_id: Optional[str]

class VenueOut(VenueBase):
    id: int

    class Config:
        from_attributes = True
