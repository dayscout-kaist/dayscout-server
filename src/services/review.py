from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import ReviewModel, engine
from src.schemas import ReviewCreateBody, UserInfoSession


def create_review(body: ReviewCreateBody, userInfo: UserInfoSession) -> int:
    review = ReviewModel(
        food_id=body.food_id,
        carbohydrate=body.nutrients.carbohydrate,
        protein=body.nutrients.protein,
        fat=body.nutrients.fat,
        sugar=body.nutrients.sugar,
        energy=body.nutrients.energy,
        user_id=userInfo["id"],
    )
    try:
        with Session(engine) as session:
            session.add(review)
            session.commit()
            session.refresh(review)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict")

    return review.id
