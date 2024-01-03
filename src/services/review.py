from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from sqlmodel import Session, select

from src.models import HistoryModel, HistoryTagModel, engine
from src.schemas import CurrentUser, Nutrients, Review, ReviewCreateBody, Tag
from src.utils.time import kst


def create_review(body: ReviewCreateBody, current_user: CurrentUser) -> int:
    review = HistoryModel(
        food_id=body.food_id,
        carbohydrate=body.nutrients.carbohydrate,
        protein=body.nutrients.protein,
        fat=body.nutrients.fat,
        sugar=body.nutrients.sugar,
        energy=body.nutrients.energy,
        user_id=current_user.id,
        content=body.content,
    )
    try:
        with Session(engine) as session:
            session.add(review)
            session.commit()
            session.refresh(review)

    except IntegrityError:
        raise HTTPException(status_code=404, detail="Not Found")

    try:
        with Session(engine) as session:
            for tag_id in body.tag_ids:
                post_tag = HistoryTagModel(review_id=review.id, tag_id=tag_id)
                session.add(post_tag)
            session.commit()

    except IntegrityError:
        pass

    return review.id


def search_review(*queries) -> list[Review]:
    with Session(engine) as session:
        posts = (
            session.exec(
                select(HistoryModel)
                .where(*queries)
                .options(
                    joinedload(HistoryModel.review_tags).joinedload(HistoryTagModel.tag)
                )
            )
            .unique()
            .all()
        )
        posts = [
            Review(
                id=post.id,
                content=post.content,
                food_id=post.food_id,
                user_id=post.user_id,
                created_at=post.created_at,
                nutrients=Nutrients(
                    carbohydrate=post.carbohydrate,
                    protein=post.protein,
                    fat=post.fat,
                    sugar=post.sugar,
                    energy=post.energy,
                ),
                tags=[
                    Tag(
                        id=reviewTag.tag.id,
                        name=reviewTag.tag.name,
                        color_background=reviewTag.tag.color_background,
                        color_border=reviewTag.tag.color_border,
                    )
                    for reviewTag in post.review_tags
                ],
            )
            for post in posts
        ]

    return posts


def search_review_by_food_id(food_id: int) -> list[Review]:
    return search_review(HistoryModel.food_id == food_id)


def search_review_by_day(datestr: str, current_user: CurrentUser) -> list[Review]:
    print(datestr)
    date = datetime.strptime(datestr, "%Y%m%d").astimezone(kst)
    return search_review(
        HistoryModel.user_id == current_user.id,
        HistoryModel.created_at >= date - timedelta(hours=9),
        HistoryModel.created_at < date + timedelta(days=1) - timedelta(hours=9),
    )
