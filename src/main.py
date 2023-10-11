from fastapi import FastAPI

from src.api import food

app = FastAPI()

app.include_router(food.router, prefix="/food", tags=["food"])
