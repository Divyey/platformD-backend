from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.event import EventCreate, EventOut
from app.db.session import get_session
from app.crud import events as event_crud
from app.core.security import get_current_user
from app.schemas.user import UserOut

router = APIRouter()

@router.post("/", response_model=EventOut, status_code=status.HTTP_201_CREATED)
async def create_event(
    event_in: EventCreate,
    current_user: UserOut = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    """
    Create a new event by the current authenticated user.
    """
    event = await event_crud.create_event(db=db, event_in=event_in, organizer_id=current_user.id)
    return event


@router.get("/", response_model=List[EventOut])
async def list_events(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_session),
):
    """
    List events with pagination.
    """
    events = await event_crud.get_events(db=db, skip=skip, limit=limit)
    return events


@router.get("/{event_id}", response_model=EventOut)
async def get_event(
    event_id: int,
    db: AsyncSession = Depends(get_session),
):
    """
    Get event details by ID.
    """
    event = await event_crud.get_event_by_id(db=db, event_id=event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(
    event_id: int,
    current_user: UserOut = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    """
    Delete an event by ID; only organizer can delete.
    """
    event = await event_crud.get_event_by_id(db=db, event_id=event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if event.organizer_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this event")
    await event_crud.delete_event(db=db, event_id=event_id)
    return None
