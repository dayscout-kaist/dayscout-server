from sqlmodel import Session, select

from src.models import PostModel, engine
from src.schemas import Post, PostCreateBody


def create_post(body: PostCreateBody) -> bool:
    post = PostModel.from_orm(body)
    with Session(engine) as session:
        session.add(post)
        session.commit()
    return True


def search_post_by_food_id(food_id: int) -> list[Post]:
    return [
        Post(
            id=1, content="test", food_id=1, user_id=1, created_at="2021-09-16 00:00:00"
        )
    ]
