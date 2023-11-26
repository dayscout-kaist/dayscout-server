from fastapi import APIRouter, HTTPException

from src.schemas import FoodCreateBody, FoodDetail, FoodEditBody, ReportConfirmBody
from src.services import (
    confirm_report,
    create_food,
    edit_food,
    get_food_detail,
    report_food,
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


@router.get("/search/byText")
async def search_by_text(text: str) -> list[FoodDetail]:
    return await search_food_by_text(text)


@router.get("/search/byBarcode")
async def search_by_barcode(barcode: int) -> FoodDetail:
    return await search_food_by_barcode(barcode)


@router.post("/review")
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
