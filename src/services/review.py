from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import ReviewModel, engine
from src.schemas import CurrentUser, ReviewCreateBody


def create_review(body: ReviewCreateBody, current_user: CurrentUser) -> int:
    review = ReviewModel(
        food_id=body.food_id,
        carbohydrate=body.nutrients.carbohydrate,
        protein=body.nutrients.protein,
        fat=body.nutrients.fat,
        sugar=body.nutrients.sugar,
        energy=body.nutrients.energy,
        user_id=current_user.id,
    )
    try:
        with Session(engine) as session:
            session.add(review)
            session.commit()
            session.refresh(review)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict")

    return review.id
