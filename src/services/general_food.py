from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import FoodInfo, engine
from src.schemas import FoodCreateBody


def create_food(body: FoodCreateBody):
    food = FoodInfo.from_orm(body)
    try:
        with Session(engine) as session:
            session.add(food)
            session.commit()
            session.refresh(food)

        return True
    except IntegrityError:
        return False
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Intentional server error")
