from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base import Base

class OrganizerProfile(Base):
    __tablename__ = "organizer_profiles"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    company_name = Column(String, nullable=True)
    contact_info = Column(String, nullable=True)  # Or JSON
    ratings = Column(Float, nullable=True)
    reviews = Column(String, nullable=True)      # Or JSON
    social_links = Column(String, nullable=True) # Or JSON/List
