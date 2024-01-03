from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from src.models import FoodModel, HistoryModel, ReportModel, engine
from src.schemas import (
    DistributionFoodContent,
    FoodCreateBody,
    FoodDetail,
    GeneralFoodContent,
    Nutrients,
    Tag,
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


def calculate_nutrient(values=()) -> float | None:
    values = list(filter(lambda x: x != None, values))
    if len(values) == 0:
        return None
    return sum(values) / len(values)


def get_general_food_detail(food: FoodModel) -> FoodDetail:
    with Session(engine) as session:
        reports = (
            session.query(ReportModel).filter(ReportModel.food_id == food.id).all()
        )
        tag_list = get_tags_by_food_id(food.id, session)

    original_nutrients = Nutrients(
        carbohydrate=food.carbohydrate,
        protein=food.protein,
        fat=food.fat,
        sugar=food.sugar,
        energy=food.energy,
    )
    reports.append(original_nutrients)
    nutrients = Nutrients(
        carbohydrate=calculate_nutrient([report.carbohydrate for report in reports]),
        protein=calculate_nutrient([report.protein for report in reports]),
        fat=calculate_nutrient([report.fat for report in reports]),
        sugar=calculate_nutrient([report.sugar for report in reports]),
        energy=calculate_nutrient([report.energy for report in reports]),
    )

    return FoodDetail(
        id=food.id,
        name=food.name,
        tag=tag_list,
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
        reports = (
            session.query(ReportModel).filter(ReportModel.food_id == food.id).all()
        )
        tag_list = get_tags_by_food_id(food.id, session)

    suggested_nutrients = (
        Nutrients(
            carbohydrate=reports[0].carbohydrate,
            protein=reports[0].protein,
            fat=reports[0].fat,
            sugar=reports[0].sugar,
            energy=reports[0].energy,
        )
        if len(reports) > 0
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
        tag=tag_list,
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


def get_tags_by_food_id(id: int, session: Session) -> list[Tag]:
    post = session.exec(select(HistoryModel).where(HistoryModel.food_id == id)).first()
    tag_list = []
    if post is not None:
        tags = post.review_tags
        for tag in tags:
            tag_list.append(tag.tag)

    return tag_list
