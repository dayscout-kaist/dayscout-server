from fastapi import APIRouter, HTTPException, UploadFile

from src.schemas import Food, FoodContentOptional, FoodInfo, FoodName
from src.services import (
    create_food,
    get_product_name_from_barcode,
    parse_nutrients_from_image,
    search_food_by_text,
)

router = APIRouter()


@router.get("/search")
async def search_by_text(query: str) -> list[FoodInfo]:
    return await search_food_by_text(query)


@router.get("/search/barcode")
async def search_by_barcode(code: int) -> FoodName:
    food_name = await get_product_name_from_barcode(code)
    return FoodName(name=food_name)


@router.post("/ocr")
async def search_by_image(file: UploadFile) -> FoodContentOptional:
    image = await file.read()
    return await parse_nutrients_from_image(image)


@router.post("/create")
async def create(body: Food) -> bool:
    if create_food(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")
