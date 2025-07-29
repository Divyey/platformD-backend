from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete

from app.db.models.event import Event
from app.schemas.event import EventCreate


async def create_event(db: AsyncSession, event_in: EventCreate, organizer_id: int) -> Event:
    """Create an event with the given organizer ID."""
    event = Event(
        organizer_id=organizer_id,
        community_id=event_in.community_id,
        title=event_in.title,
        description=event_in.description,
        event_date=event_in.event_date,
        event_time=event_in.event_time,
        location=event_in.location,
        mode=event_in.mode,
        category=event_in.category,
        subcategories=event_in.subcategories,
        banner_image_url=event_in.banner_image_url,
        # image_urls not stored currently in DB
    )
    db.add(event)
    await db.commit()
    await db.refresh(event)
    return event


async def get_event_by_id(db: AsyncSession, event_id: int) -> Optional[Event]:
    """Get event by ID."""
    result = await db.execute(select(Event).where(Event.id == event_id))
    return result.scalar_one_or_none()


async def get_events(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Event]:
    """List events with pagination."""
    result = await db.execute(select(Event).offset(skip).limit(limit))
    return result.scalars().all()


async def delete_event(db: AsyncSession, event_id: int) -> bool:
    """Delete event by ID. Return True if deleted, False otherwise."""
    result = await db.execute(select(Event).where(Event.id == event_id))
    event = result.scalar_one_or_none()
    if event is None:
        return False
    await db.delete(event)
    await db.commit()
    return True
