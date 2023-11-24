from fastapi import APIRouter, HTTPException

from src.schemas import FoodCreateBody, FoodDetail, FoodEditBody, ReportConfirmBody
from src.services import (
    confirm_report,
    create_food,
    edit_food,
    get_product_name_from_barcode,
    inquiry_food,
    report_food,
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


@router.get("/detail/{food_id}")
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
