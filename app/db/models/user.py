from typing import List, Optional
from sqlalchemy import Integer, String, Boolean, DateTime, ARRAY, Text, Table, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from app.db.base import Base

# Association table for many-to-many User <-> Community membership
user_community_association = Table(
    'user_community_association',
    Base.metadata,
    mapped_column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    mapped_column('community_id', Integer, ForeignKey('communities.id'), primary_key=True),
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    contact_number: Mapped[Optional[str]] = mapped_column(nullable=True)
    hashed_password: Mapped[Optional[str]] = mapped_column(nullable=True)
    roles: Mapped[str] = mapped_column(default="user")
    google_user_id: Mapped[Optional[str]] = mapped_column(nullable=True)
    avatar_url: Mapped[Optional[str]] = mapped_column(nullable=True)
    bio: Mapped[Optional[str]] = mapped_column(nullable=True)
    interests: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), nullable=True)
    locale: Mapped[str] = mapped_column(default="en")
    is_active: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    notification_on: Mapped[bool] = mapped_column(default=True)
    notification_silent: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    last_login: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    # Relationships with eager loading for async-safe serialization
    communities_created = relationship(
        "Community",
        back_populates="creator",
        lazy="selectin"
    )
    communities = relationship(
        "Community",
        secondary=user_community_association,
        back_populates="members",
        lazy="selectin"
    )

    events = relationship("Event", back_populates="organizer", lazy="selectin")
    rsvps = relationship("RSVP", back_populates="user", lazy="selectin")
    messages_sent = relationship("Message", foreign_keys='Message.sender_id', lazy="selectin")
