from fastapi import FastAPI
from app.api.v1 import api_router

app = FastAPI(title="PlatformD Backend API")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Hello from platformD backend"}
