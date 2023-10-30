from fastapi import FastAPI

from src.api import auth, food

app = FastAPI()

app.include_router(food.router, prefix="/food", tags=["food"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
