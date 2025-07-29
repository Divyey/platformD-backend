from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()


async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    result = await db.execute(
        select(User).
        options(
            selectinload(User.communities_created),
            selectinload(User.communities),
            selectinload(User.events),
        ).
        where(User.id == user_id)
    )
    return result.scalars().first()



async def create_user(db: AsyncSession, user_data: dict, hashed_password: str) -> User:
    """
    Create a new User instance from user_data dict and hashed password,
    add to session, commit and refresh.
    """
    user = User(**user_data)
    user.hashed_password = hashed_password
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
