from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from sqlmodel import Session, select

from src.models import PostModel, PostTagModel, TagModel, engine
from src.schemas import Post, PostCreateBody, Tag, UserInfoSession


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

    try:
        with Session(engine) as session:
            for tag_id in body.tag_ids:
                post_tag = PostTagModel(post_id=post.id, tag_id=tag_id)
                session.add(post_tag)
            session.commit()

    except IntegrityError:
        pass

    return post.id


def search_post_by_food_id(food_id: int) -> list[Post]:
    with Session(engine) as session:
        posts = (
            session.exec(
                select(PostModel)
                .where(PostModel.food_id == food_id)
                .options(joinedload(PostModel.post_tags).joinedload(PostTagModel.tag))
            )
            .unique()
            .all()
        )
        posts = [
            Post(
                id=post.id,
                content=post.content,
                food_id=post.food_id,
                user_id=post.user_id,
                created_at=post.created_at,
                tags=[
                    Tag(
                        id=postTag.tag.id,
                        name=postTag.tag.name,
                        color_background=postTag.tag.color_background,
                        color_border=postTag.tag.color_border,
                    )
                    for postTag in post.post_tags
                ],
            )
            for post in posts
        ]

    return posts
