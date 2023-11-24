from fastapi import HTTPException
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session

from src.models import FoodModel, ReviewModel, engine
from src.schemas import (
    AbsoluteUnit,
    DistributionFoodContent,
    FoodCreateBody,
    FoodDetail,
    GeneralFoodContent,
    Nutrients,
)
from src.services.product_db import (
    get_product_by_id,
    get_product_from_barcode,
    get_product_list,
)


def create_food(body: FoodCreateBody):
    food = FoodModel.from_orm(body)
    try:
        with Session(engine) as session:
            session.add(food)
            session.commit()
            session.refresh(food)

    except IntegrityError:
        return False

    return True


def inquiry_general(food_info: FoodModel, food_id: int, session: Session):
    edit_info = session.query(ReviewModel).filter(ReviewModel.food_id == food_id).all()
    carbohydrate_avg = (
        food_info.carbohydrate + sum(edit.carbohydrate for edit in edit_info)
    ) / (len(edit_info) + 1)

    protein_avg = (food_info.protein + sum(edit.protein for edit in edit_info)) / (
        len(edit_info) + 1
    )

    fat_avg = (food_info.fat + sum(edit.fat for edit in edit_info)) / (
        len(edit_info) + 1
    )

    sugar_avg = (food_info.sugar + sum(edit.sugar for edit in edit_info)) / (
        len(edit_info) + 1
    )

    energy_avg = (food_info.energy + sum(edit.energy for edit in edit_info)) / (
        len(edit_info) + 1
    )

    if not food_info:
        raise HTTPException(status_code=404, detail="Food not found")
    FoodInfo_Pydantic = sqlalchemy_to_pydantic(FoodModel, exclude=["id"])
    food_info = FoodInfo_Pydantic(**food_info.__dict__)

    nutrients = Nutrients(
        carbohydrate=carbohydrate_avg,
        protein=protein_avg,
        fat=fat_avg,
        sugar=sugar_avg,
        energy=energy_avg,
    )

    original_nutrients = Nutrients(
        carbohydrate=food_info.carbohydrate,
        protein=food_info.protein,
        fat=food_info.fat,
        sugar=food_info.sugar,
        energy=food_info.energy,
    )
    content = GeneralFoodContent(
        type="general",
        totalWeight=food_info.total_weight,
        unit="absolute",
        representName=food_info.represent_name,
        className=food_info.class_name,
        primaryUnit="g",
        nutrients=nutrients,
        originalNutrients=original_nutrients,
    )
    food_detail = FoodDetail(
        id=food_id,
        name=food_info.name,
        tag=[],
        content=content,
        image_src=food_info.image_src,
    )

    return food_detail


def inquiry_distribution(food_info: FoodModel, food_id: int, session: Session):
    review_info = (
        session.query(ReviewModel).filter(ReviewModel.food_id == food_id).first()
    )
    if not food_info:
        raise HTTPException(status_code=404, detail="Food not found")
    FoodInfo_Pydantic = sqlalchemy_to_pydantic(FoodModel, exclude=["id"])
    food_info = FoodInfo_Pydantic(**food_info.__dict__)
    suggested_nutrients = None
    if review_info:
        ReviewInfo_Pydantic = sqlalchemy_to_pydantic(ReviewModel, exclude=["id"])
        review_info = ReviewInfo_Pydantic(**review_info.__dict__)
        suggested_nutrients = Nutrients(
            carbohydrate=review_info.carbohydrate,
            protein=review_info.protein,
            fat=review_info.fat,
            sugar=review_info.sugar,
            energy=review_info.energy,
        )

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
        suggestedNutrients=suggested_nutrients,
    )
    food_detail = FoodDetail(
        id=food_id,
        name=food_info.name,
        tag=[],
        content=content,
        image_src=food_info.image_src,
    )
    return food_detail


def inquiry_food(food_id: int):
    try:
        with Session(engine) as session:
            food_info = session.query(FoodModel).filter(FoodModel.id == food_id).first()
            if food_info.type == "general":
                return inquiry_general(food_info, food_id, session)
            else:
                return inquiry_distribution(food_info, food_id, session)

    except IntegrityError:
        return False


async def get_product_by_text(text: str) -> list[FoodDetail]:
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


async def get_product_by_barcode(barcode_number: float) -> FoodDetail:
    try:
        with Session(engine) as session:
            food_info = (
                session.query(FoodModel)
                .filter(FoodModel.barcode_number == barcode_number)
                .first()
            )
            if food_info:
                pass
            else:
                food_info = await get_product_from_barcode(int(barcode_number))
                session.add(food_info)
                session.commit()
            food = inquiry_distribution(food_info, food_info.id, session)
            return food

    except IntegrityError:
        raise HTTPException(status_code=404, detail="Not food Found")
