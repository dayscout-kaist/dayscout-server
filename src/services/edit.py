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

        return True
    except IntegrityError:
        return False
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Intentional server error")
