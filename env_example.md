# .env - example for production/development

# FastAPI settings
API_PREFIX=/api/v1
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Database (async)
DATABASE_URL=postgresql+asyncpg://username:password@localhost/DatabaseName

# OAuth/SSO (optional)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# OpenAI/LLM API keys (for later AI features)
OPENAI_KEY_1=sk-...
OPENAI_KEY_2=sk-...
OPENAI_KEY_3=sk-...
OPENAI_KEY_4=sk-...
OPENAI_KEY_5=sk-...

# Optional: Add other keys as needed
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
SMTP_SERVER=smtp.example.com
SMTP_USER=your_email@example.com
SMTP_PASSWORD=your_email_password


# Redis/VectorDB (future phases, optional)
REDIS_URL=redis://localhost:6379
VECTOR_DB_URL=http://localhost:8000

