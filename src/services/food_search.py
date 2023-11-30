import asyncio

from fastapi import HTTPException
from sqlalchemy import func
from sqlmodel import Session, select

from src.models import FoodModel, PostModel, TagModel, engine
from src.schemas import Food, FoodDetail
from src.services.product_db import (
    get_product_by_id,
    get_product_from_barcode,
    get_product_list,
)

from .food import get_distribution_food_detail, get_tags_by_food_id


async def create_food_by_product_id(product_id: int) -> int | None:
    try:
        food = await get_product_by_id(product_id)
        with Session(engine) as session:
            session.add(food)
            session.commit()
            session.refresh(food)

    except Exception:
        return None

    return food.id


async def search_food_by_text(text: str) -> list[Food]:
    products = await get_product_list(text)
    await asyncio.gather(
        *[create_food_by_product_id(product.id) for product in products]
    )

    with Session(engine) as session:
        foods = session.exec(
            select(FoodModel).where(FoodModel.name.ilike(f"%{text}%"))
        ).all()
        print(foods)
        tag_dict = {}

        for food in foods:
            tag_list = get_tags_by_food_id(food.id, session)
            tag_dict[food.id] = tag_list

    return [
        Food(
            id=food.id,
            name=food.name,
            tag=tag_dict[food.id],
            representName=food.represent_name,
            className=food.class_name,
            image_src=food.image_src,
        )
        for food in foods
    ]


async def search_food_by_barcode(barcode: str) -> FoodDetail:
    with Session(engine) as session:
        food = (
            session.query(FoodModel).filter(FoodModel.barcode_number == barcode).first()
        )

    if food == None:
        try:
            food = await get_product_from_barcode(int(barcode))
        except Exception:
            raise HTTPException(status_code=404, detail="Not food Found")

        with Session(engine) as session:
            session.add(food)
            session.commit()
            session.refresh(food)

    return get_distribution_food_detail(food)
