from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as api_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.version
)

app.include_router(api_router)
