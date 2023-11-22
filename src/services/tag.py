from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import TagModel, engine
from src.schemas import TagCreateBody
from src.schemas import TagInfo as Tag


def search_all_tags() -> list[Tag]:
    with Session(engine) as session:
        return session.query(TagModel).all()


def create_tag(body: TagCreateBody) -> bool:
    try:
        tag = TagModel.from_orm(body)
        with Session(engine) as session:
            session.add(tag)
            session.commit()

    except IntegrityError:
        return False

    return True


def remove_tag_by_id(id: int) -> bool:
    with Session(engine) as session:
        tag = session.get(TagModel, id)
        if tag is None:
            return False
        session.delete(tag)
        session.commit()
    return True
