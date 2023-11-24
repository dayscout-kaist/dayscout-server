from fastapi import APIRouter, HTTPException

from src.schemas import FoodCreateBody, FoodDetail, FoodEditBody, ReportConfirmBody
from src.services import (
    confirm_report,
    create_food,
    edit_food,
    get_product_by_barcode,
    get_product_by_text,
    inquiry_food,
    report_food,
)

router = APIRouter()


@router.get("/search/text")
async def search_by_text(text: str) -> list[FoodDetail]:
    return await get_product_by_text(text)


@router.get("/search/barcode")
async def search_by_barcode(barcode_number: float) -> FoodDetail:
    return await get_product_by_barcode(barcode_number)
    # food_name = await get_product_name_from_barcode(q)
    # return FoodName(name=food_name)


@router.get("/detail")
async def inquiry(food_id: int) -> FoodDetail:
    food_detail = inquiry_food(food_id)
    if food_detail:
        return food_detail
    raise HTTPException(status_code=409, detail="Conflict")


@router.post("/create")
async def create(body: FoodCreateBody) -> bool:
    if create_food(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")


@router.post("/edit")
async def edit(body: FoodEditBody) -> bool:
    if edit_food(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")


@router.post("/report")
async def edit(body: FoodEditBody) -> bool:
    if report_food(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")


@router.post("/report/confirm")
async def confirm(body: ReportConfirmBody) -> bool:
    if confirm_report(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")
