from fastapi import FastAPI
from app.api.v1 import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PlatformD Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",        # React dev server (CRA) or similar
        "http://localhost:5173",        # Vite dev server default
        "https://platform-d-frontend-z1b1.vercel.app"  # Your deployed frontend URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Hello from platformD backend"}
