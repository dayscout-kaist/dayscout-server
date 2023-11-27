from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import TagModel, engine
from src.schemas import Tag, TagCreateBody


def search_all_tags() -> list[Tag]:
    with Session(engine) as session:
        return session.query(TagModel).all()


def create_tag(body: TagCreateBody) -> int:
    try:
        tag = TagModel.from_orm(body)
        with Session(engine) as session:
            session.add(tag)
            session.commit()
            session.refresh(tag)

    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict")

    return tag.id


def remove_tag_by_id(id: int) -> int:
    with Session(engine) as session:
        tag = session.get(TagModel, id)
        if tag is None:
            raise HTTPException(status_code=404, detail="Not Found")
        session.delete(tag)
        session.commit()

    return id
