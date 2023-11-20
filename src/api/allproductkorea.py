from fastapi import APIRouter

from src.services.product_db import (
    get_product_by_id,
    get_product_from_barcode,
    get_product_list,
)

router = APIRouter()


@router.get("/get_product_list")
async def wrap_get_product_list(keyword: str | int):
    return await get_product_list(keyword)


@router.get("/get_product_by_id")
async def wrap_get_product_by_id(id: int):
    return await get_product_by_id(id)


@router.get("/get_product_from_barcode")
async def wrap_get_product_from_barcode(barcode: int):
    return await get_product_from_barcode(barcode)
