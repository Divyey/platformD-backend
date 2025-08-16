from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.community import Community

async def create_community(db: AsyncSession, name: str, description: str, creator_id: int) -> Community:
    community = Community(
        name=name,
        description=description,
        creator_id=creator_id
    )
    db.add(community)
    await db.commit()
    await db.refresh(community)
    return community

async def get_community_by_id(db: AsyncSession, community_id: int):
    result = await db.execute(select(Community).where(Community.id == community_id))
    return result.scalar_one_or_none()

async def get_communities(db: AsyncSession, skip: int = 0, limit: int = 20):
    query = select(Community).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
