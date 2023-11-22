from fastapi import APIRouter, HTTPException

from src.schemas import FoodCreateBody, FoodDetail
from src.services import (
    create_food,
    get_product_name_from_barcode,
    inquiry_food,
    search_food_by_text,
)

router = APIRouter()


@router.get("/search/text")
async def search_by_text(q: str) -> list[FoodDetail]:
    return await search_food_by_text(q)


@router.get("/search/barcode")
async def search_by_barcode(q: int) -> list[FoodDetail]:
    return []
    # food_name = await get_product_name_from_barcode(q)
    # return FoodName(name=food_name)


@router.post("/create")
async def create(body: FoodCreateBody) -> bool:
    if create_food(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")


@router.get("/detail/{food_id}")
async def inquiry(food_id: int) -> FoodDetail:
    food_detail = inquiry_food(food_id)
    if food_detail:
        return food_detail
    raise HTTPException(status_code=409, detail="Conflict")
