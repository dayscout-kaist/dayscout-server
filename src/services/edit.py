from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import EditModel, engine
from src.schemas import FoodEditBody


def edit_food(body: FoodEditBody):
    Edit = EditModel.from_orm(body)
    try:
        with Session(engine) as session:
            session.add(Edit)
            session.commit()
            session.refresh(Edit)

    except IntegrityError:
        return False

    return True
