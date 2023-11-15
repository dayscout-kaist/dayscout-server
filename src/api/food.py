from fastapi import APIRouter

from src.schemas import FoodInfo, FoodName
from src.services import get_product_name_from_barcode, search_food_by_text

router = APIRouter()


@router.get("/search")
async def search_by_text(query: str) -> list[FoodInfo]:
    return await search_food_by_text(query)


@router.get("/search/barcode")
async def search_by_barcode(code: int) -> FoodName:
    food_name = await get_product_name_from_barcode(code)
    return FoodName(name=food_name)
