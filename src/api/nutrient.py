from fastapi import APIRouter, UploadFile

from src.schemas import FoodContentOptional
from src.services import parse_nutrients_from_image

router = APIRouter()


@router.post("/ocr")
async def search_by_image(file: UploadFile) -> FoodContentOptional:
    image = await file.read()
    return await parse_nutrients_from_image(image)
