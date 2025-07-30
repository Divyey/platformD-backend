from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.auth_google import router as auth_google_router
from app.api.v1.endpoints.users import router as users_router
from app.api.v1.endpoints.events import router as events_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(auth_google_router, prefix="/auth/google", tags=["auth_google"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(events_router, prefix="/events", tags=["events"])
