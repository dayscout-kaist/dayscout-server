from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from src.api import auth, food

from .settings import settings

app = FastAPI()

app.add_middleware(
    SessionMiddleware, secret_key=settings.SESSION_SECRET_KEY, max_age=None
)
app.include_router(food.router, prefix="/food", tags=["food"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
