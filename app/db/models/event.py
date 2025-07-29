from sqlalchemy import Column, Integer, String, Text, Float, Date, Time, Enum, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.db.base import Base

class EventMode(PyEnum):
    online = "online"
    offline = "offline"
    both = "both"

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    organizer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    community_id = Column(Integer, ForeignKey("communities.id"), nullable=True)
    organizer_rating = Column(Float, nullable=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    event_date = Column(Date, nullable=False)
    event_time = Column(Time, nullable=True)
    location = Column(String, nullable=False)
    mode = Column(Enum(EventMode), default=EventMode.offline)
    banner_image_url = Column(String, nullable=True)
    category = Column(String, nullable=False)
    subcategories = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    organizer = relationship("User", back_populates="events")
    community = relationship("Community", back_populates="events")
    rsvps = relationship("RSVP", back_populates="event")

    # # For future:
    # event_images = relationship('EventImage', back_populates='event')

# # In future, consider:
# class EventImage(Base):
#     __tablename__ = "event_images"
#     id = Column(Integer, primary_key=True)
#     event_id = Column(Integer, ForeignKey("events.id"))
#     image_url = Column(String, nullable=False)
#     description = Column(String, nullable=True)
