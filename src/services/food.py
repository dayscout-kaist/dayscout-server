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
        unit=AbsoluteUnit(),
        primaryUnit="g",
        nutrients=nutrients,
        originalNutrients=original_nutrients,
    )
    food_detail = FoodDetail(id=food_id, name=food_info.name, tag=[], content=content)

    return food_detail


def inquiry_distribution(food_info: FoodModel, food_id: int, session: Session):
    review_info = (
        session.query(ReviewModel).filter(ReviewModel.food_id == food_id).first()
    )
    if not food_info:
        raise HTTPException(status_code=404, detail="Food not found")
    FoodInfo_Pydantic = sqlalchemy_to_pydantic(FoodModel, exclude=["id"])
    food_info = FoodInfo_Pydantic(**food_info.__dict__)
    ReviewInfo_Pydantic = sqlalchemy_to_pydantic(ReviewModel, exclude=["id"])
    review_info = ReviewInfo_Pydantic(**review_info.__dict__)

    nutrients = Nutrients(
        carbohydrate=food_info.carbohydrate,
        protein=food_info.protein,
        fat=food_info.fat,
        sugar=food_info.sugar,
        energy=food_info.energy,
    )

    suggested_nutrients = Nutrients(
        carbohydrate=review_info.carbohydrate,
        protein=review_info.protein,
        fat=review_info.fat,
        sugar=review_info.sugar,
        energy=review_info.energy,
    )
    content = DistributionFoodContent(
        type="distribution",
        totalWeight=food_info.total_weight,
        manufacturer=food_info.manufacturer,
        category=food_info.category,
        unit=food_info.unit,
        primaryUnit=food_info.primary_unit,
        nutrients=nutrients,
        suggested_nutrients=suggested_nutrients,
    )
    food_detail = FoodDetail(id=food_id, name=food_info.name, tag=[], content=content)
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
