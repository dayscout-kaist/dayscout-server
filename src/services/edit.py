from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import ReviewModel, engine
from src.schemas import FoodEditBody


def edit_food(body: FoodEditBody):
    edit = ReviewModel.from_orm(body)
    try:
        with Session(engine) as session:
            session.add(edit)
            session.commit()
            session.refresh(edit)

        return True
    except IntegrityError:
        return False
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Intentional server error")
