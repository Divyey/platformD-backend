from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.community import CommunityCreate, CommunityOut
from app.db.session import get_session
from app.crud import community as community_crud
from app.core.security import get_current_user
from app.schemas.user import UserOut

router = APIRouter()

@router.post("/", response_model=CommunityOut, status_code=status.HTTP_201_CREATED)
async def create_community(
    community_in: CommunityCreate,
    current_user: UserOut = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    existing = await community_crud.get_community_by_id(db, community_in.name)
    if existing:
        raise HTTPException(status_code=400, detail="Community with this name already exists")
    community = await community_crud.create_community(
        db=db,
        name=community_in.name,
        description=community_in.description,
        creator_id=current_user.id
    )
    return community

@router.get("/", response_model=List[CommunityOut])
async def list_communities(
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_session)
):
    return await community_crud.get_communities(db, skip=skip, limit=limit)

@router.get("/{community_id}", response_model=CommunityOut)
async def get_community(
    community_id: int,
    db: AsyncSession = Depends(get_session)
):
    community = await community_crud.get_community_by_id(db, community_id)
    if not community:
        raise HTTPException(status_code=404, detail="Community not found")
    return community
