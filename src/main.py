from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from src.api import allproductkorea, auth, edit, food, nutrient

from .settings import settings

app = FastAPI()

app.add_middleware(
    SessionMiddleware, secret_key=settings.SESSION_SECRET_KEY, max_age=7200
)
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(food.router, prefix="/food", tags=["food"])
app.include_router(nutrient.router, prefix="/nutrient", tags=["nutrient"])
app.include_router(edit.router, prefix="/edit", tags=["edit"])
app.include_router(
    allproductkorea.router, prefix="/allproductkorea", tags=["allproductkorea"]
)
