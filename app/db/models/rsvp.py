from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.db.base import Base

class RSVPStatus(PyEnum):
    going = "going"
    interested = "interested"
    declined = "declined"

class RSVP(Base):
    __tablename__ = "rsvps"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    status = Column(Enum(RSVPStatus), default=RSVPStatus.interested)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="rsvps")
    event = relationship("Event", back_populates="rsvps")
