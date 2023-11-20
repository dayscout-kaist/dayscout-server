from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import TagInfo, engine
from src.schemas import TagCreateBody
from src.schemas import TagInfo as Tag


def search_all_tags() -> list[Tag]:
    with Session(engine) as session:
        return session.query(TagInfo).all()


def create_tag(body: TagCreateBody) -> bool:
    try:
        tag = TagInfo.from_orm(body)
        with Session(engine) as session:
            session.add(tag)
            session.commit()
        return True
    except IntegrityError:
        return False
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Intentional server error")


def remove_tag_by_id(id: int) -> bool:
    with Session(engine) as session:
        tag = session.get(TagInfo, id)
        if tag is None:
            return False
        session.delete(tag)
        session.commit()
    return True
