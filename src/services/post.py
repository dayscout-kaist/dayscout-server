from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import PostModel, engine
from src.schemas import Post, PostCreateBody, UserInfoSession


def create_post(body: PostCreateBody, userInfo: UserInfoSession) -> int:
    try:
        with Session(engine) as session:
            post = PostModel(
                content=body.content,
                food_id=body.food_id,
                user_id=userInfo["id"],
            )
            session.add(post)
            session.commit()
            session.refresh(post)

    except IntegrityError:
        raise HTTPException(status_code=404, detail="Not Found")

    return post.id


def search_post_by_food_id(food_id: int) -> list[Post]:
    return [
        Post(
            id=1, content="test", food_id=1, user_id=1, created_at="2021-09-16 00:00:00"
        )
    ]
