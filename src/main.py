from fastapi import FastAPI

from src.api import food, user

app = FastAPI()

app.include_router(food.router, prefix="/food", tags=["food"])
app.include_router(user.router, prefix="/user", tags=["user"])
