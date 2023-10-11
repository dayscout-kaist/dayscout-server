from fastapi import APIRouter, UploadFile

from src.schemas import FoodContentOptional, FoodInfo
from src.services import parse_nutrients_from_image, search_food_by_text

router = APIRouter()


@router.get("/search")
async def search_by_text(query: str) -> list[FoodInfo]:
    return await search_food_by_text(query)


@router.get("/search/barcode")
async def search_by_barcode(code: str) -> list[FoodInfo]:
    return []  # TODO


@router.post("/ocr")
async def search_by_image(file: UploadFile) -> FoodContentOptional:
    image = await file.read()
    return await parse_nutrients_from_image(image)
