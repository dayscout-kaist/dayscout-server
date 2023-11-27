from fastapi import HTTPException
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from src.models import FoodModel, ReviewModel, engine
from src.schemas import (
    DistributionFoodContent,
    FoodCreateBody,
    FoodDetail,
    GeneralFoodContent,
    Nutrients,
)


def create_food(body: FoodCreateBody) -> int:
    try:
        with Session(engine) as session:
            food = FoodModel.from_orm(body)
            session.add(food)
            session.commit()
            session.refresh(food)

    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict")

    return food.id


def calculate_nutrient(values=[]) -> float | None:
    values = list(filter(lambda x: x != None, values))
    if len(values) == 0:
        return None
    return sum(values) / len(values)


def get_general_food_detail(food: FoodModel) -> FoodDetail:
    with Session(engine) as session:
        reviews = (
            session.query(ReviewModel).filter(ReviewModel.food_id == food.id).all()
        )

    original_nutrients = Nutrients(
        carbohydrate=food.carbohydrate,
        protein=food.protein,
        fat=food.fat,
        sugar=food.sugar,
        energy=food.energy,
    )
    reviews.append(original_nutrients)
    nutrients = Nutrients(
        carbohydrate=calculate_nutrient([review.carbohydrate for review in reviews]),
        protein=calculate_nutrient([review.protein for review in reviews]),
        fat=calculate_nutrient([review.fat for review in reviews]),
        sugar=calculate_nutrient([review.sugar for review in reviews]),
        energy=calculate_nutrient([review.energy for review in reviews]),
    )

    return FoodDetail(
        id=food.id,
        name=food.name,
        tag=[],
        content=GeneralFoodContent(
            total_weight=food.total_weight,
            unit="absolute",
            represent_name=food.represent_name,
            class_name=food.class_name,
            primary_unit="g",
            nutrients=nutrients,
            original_nutrients=original_nutrients,
        ),
        image_src=food.image_src,
    )


def get_distribution_food_detail(food: FoodModel) -> FoodDetail:
    with Session(engine) as session:
        reviews = (
            session.query(ReviewModel).filter(ReviewModel.food_id == food.id).all()
        )

    suggested_nutrients = (
        Nutrients(
            carbohydrate=reviews[0].carbohydrate,
            protein=reviews[0].protein,
            fat=reviews[0].fat,
            sugar=reviews[0].sugar,
            energy=reviews[0].energy,
        )
        if len(reviews) > 0
        else None
    )

    nutrients = Nutrients(
        carbohydrate=food.carbohydrate,
        protein=food.protein,
        fat=food.fat,
        sugar=food.sugar,
        energy=food.energy,
    )
    return FoodDetail(
        id=food.id,
        name=food.name,
        tag=[],
        content=DistributionFoodContent(
            total_weight=food.total_weight,
            manufacturer=food.manufacturer,
            represent_name=food.represent_name,
            class_name=food.class_name,
            unit=food.unit,
            primary_unit=food.primary_unit,
            nutrients=nutrients,
            suggested_nutrients=suggested_nutrients,
        ),
        image_src=food.image_src,
    )


def get_food_detail(food_id: int) -> FoodDetail:
    with Session(engine) as session:
        food = session.exec(select(FoodModel).where(FoodModel.id == food_id)).first()

    if food == None:
        raise HTTPException(status_code=404, detail="Not Food Found")

    return (
        get_general_food_detail(food)
        if food.type == "general"
        else get_distribution_food_detail(food)
    )
