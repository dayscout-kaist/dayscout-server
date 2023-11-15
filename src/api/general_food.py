from typing import Union

from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from src.models.db_food import Nutrients
from src.services.general_food import create_food

router = APIRouter()


@router.post("/food/create")
async def create_food(body: Nutrients) -> bool:
    if create_food(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")
