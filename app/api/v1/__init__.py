from fastapi import APIRouter
from app.api.v1.endpoints import auth_router, auth_google_router, users_router, events_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(auth_google_router, prefix="/auth/google", tags=["auth", "google"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(events_router, prefix="/events", tags=["events"])
