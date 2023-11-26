from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import FoodModel, engine
from src.schemas import DistributionFoodContent, FoodDetail, Nutrients
from src.services.product_db import (
    get_product_by_id,
    get_product_from_barcode,
    get_product_list,
)


async def search_food_by_text(text: str) -> list[FoodDetail]:
    try:
        with Session(engine) as session:
            food_list = []
            general_food_list = (
                session.query(FoodModel).filter(FoodModel.name.ilike(text)).all()
            )
            for general_food in general_food_list:
                food = inquiry_general(general_food, general_food.id, session)
                food_list.append(food)

            product_list = await get_product_list(text)
            for product in product_list:
                food_info = (
                    session.query(FoodModel)
                    .filter(FoodModel.barcode_number == product.barcode_number)
                    .first()
                )
                if food_info:
                    pass
                else:
                    food_info = await get_product_by_id(product.id)
                    if food_info is None:
                        continue

                    session.add(food_info)
                    session.commit()

                nutrients = Nutrients(
                    carbohydrate=food_info.carbohydrate,
                    protein=food_info.protein,
                    fat=food_info.fat,
                    sugar=food_info.sugar,
                    energy=food_info.energy,
                )
                content = DistributionFoodContent(
                    type="distribution",
                    totalWeight=food_info.total_weight,
                    manufacturer=food_info.manufacturer,
                    representName=food_info.represent_name,
                    className=food_info.class_name,
                    unit=food_info.unit,
                    primaryUnit=food_info.primary_unit,
                    nutrients=nutrients,
                )

                food_detail = FoodDetail(
                    id=food_info.id,
                    name=food_info.name,
                    tag=[],
                    content=content,
                    image_src=food_info.image_src,
                )
                food_list.append(food_detail)

            return food_list

    except IntegrityError:
        raise HTTPException(status_code=404, detail="Not food Found")


async def search_food_by_barcode(barcode: int) -> FoodDetail:
    try:
        with Session(engine) as session:
            food_info = (
                session.query(FoodModel)
                .filter(FoodModel.barcode_number == barcode)
                .first()
            )
            if food_info:
                pass
            else:
                food_info = await get_product_from_barcode(int(barcode))
                session.add(food_info)
                session.commit()
            food = inquiry_distribution(food_info, food_info.id, session)
            return food

    except IntegrityError:
        raise HTTPException(status_code=404, detail="Not food Found")
