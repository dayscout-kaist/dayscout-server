from bcrypt import checkpw, gensalt, hashpw
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from starlette.requests import Request

from src.models import Standard_food, general_food_engine


def create_food(food: Standard_food):
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
