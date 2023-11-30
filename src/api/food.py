from fastapi import APIRouter, HTTPException

from src.schemas import Food, FoodCreateBody, FoodDetail
from src.services import (
    create_food,
    get_food_detail,
    search_food_by_barcode,
    search_food_by_text,
)

router = APIRouter()


@router.post("/create")
async def create(body: FoodCreateBody) -> int:
    return create_food(body)


@router.get("/detail")
async def detail(id: int) -> FoodDetail:
    return get_food_detail(id)


@router.get("/search/byBarcode")
async def search_by_barcode(barcode: str) -> FoodDetail:
    return await search_food_by_barcode(barcode)


@router.get("/search/byText")
async def search_by_text(text: str) -> list[Food]:
    return await search_food_by_text(text)
