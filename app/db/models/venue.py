from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    zip = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    features = Column(String, nullable=True)   # JSON if using advanced features
    google_place_id = Column(String, nullable=True)
    # # For future:
    # venue_image_url = Column(String, nullable=True)
