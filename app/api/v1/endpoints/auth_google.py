from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from app.core.config import settings
from app.db.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.users import get_user_by_email, create_user
from app.core.security import create_access_token
import httpx

router = APIRouter()

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USER_INFO_URL = "https://www.googleapis.com/oauth2/v2/userinfo"


@router.get("/google-login")
async def google_login():
    # Prepare the URL to redirect user to Google OAuth consent screen
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent"
    }
    url = httpx.URL(GOOGLE_AUTH_URL).include_query_params(**params)
    return RedirectResponse(url)


@router.get("/google-callback")
async def google_callback(request: Request, db: AsyncSession = Depends(get_session)):
    # Get authorization code sent by Google
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Code not found in callback")

    # Exchange auth code for tokens
    async with httpx.AsyncClient() as client:
        token_resp = await client.post(
            GOOGLE_TOKEN_URL,
            data={
                "code": code,
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "redirect_uri": settings.GOOGLE_REDIRECT_URI,
                "grant_type": "authorization_code"
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        if token_resp.status_code != 200:
            raise HTTPException(status_code=token_resp.status_code, detail="Failed to fetch token from Google")
        tokens = token_resp.json()
        access_token = tokens.get("access_token")

        # Use access token to get user info
        user_resp = await client.get(
            GOOGLE_USER_INFO_URL,
            headers={"Authorization": f"Bearer {access_token}"}
        )
        if user_resp.status_code != 200:
            raise HTTPException(status_code=user_resp.status_code, detail="Failed to fetch user info from Google")
        user_info = user_resp.json()

    # Extract relevant info
    email = user_info.get("email")
    name = user_info.get("name") or user_info.get("given_name") or "GoogleUser"
    google_user_id = user_info.get("id")
    picture = user_info.get("picture")

    if not email:
        raise HTTPException(status_code=400, detail="Email not available from Google")

    # Check if user exists
    user = await get_user_by_email(db, email)
    if not user:
        # Create user with some defaults
        user_data = {
            "username": email.split("@")[0],
            "email": email,
            "avatar_url": picture,
            "bio": f"Google OAuth user {name}",
            "google_user_id": google_user_id,
            "roles": "user",
            "is_active": True,
            "is_verified": True,
            # Add other default fields you want; password can be None or set to unusable string
        }
        # Create user without password since OAuth users login with Google
        user = await create_user(db, user_data, hashed_password=None)

    # Generate JWT token for your own app auth with user.email as subject
    token = create_access_token(data={"sub": user.email})

    # You can redirect to frontend app with token or
    # just return the token here for simplicity:
    return {"access_token": token, "token_type": "bearer"}
