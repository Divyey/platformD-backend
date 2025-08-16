from fastapi import FastAPI
from app.api.v1 import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints.auth_google import router as auth_google_router

app = FastAPI(title="PlatformD Backend API")

origins = [
    "http://localhost:3000",            # frontend dev origin
    "http://localhost:5173",    
    "https://platform-d-frontend-z1b1.vercel.app"  # your deployed frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")
app.include_router(auth_google_router, prefix="/api/v1/auth")

@app.get("/")
def read_root():
    return {"message": "Hello from platformD backend"}
