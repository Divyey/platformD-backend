# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker
# from app.core.config import settings

# engine = create_async_engine(settings.DATABASE_URL, echo=True)

# async_session = sessionmaker(
#     bind=engine,
#     class_=AsyncSession,
#     expire_on_commit=False,
# )

# async def get_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session
import ssl
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create default SSL context
ssl_context = ssl.create_default_context()

# IMPORTANT: Ensure DATABASE_URL has 'postgresql+asyncpg://'
# and does NOT have ?sslmode=require appended
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context},  # Pass SSL context here
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
