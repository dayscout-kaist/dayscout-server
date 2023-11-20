from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import ReviewInfo, engine
from src.schemas import ReviewCreateBody


def create_review(body: ReviewCreateBody):
    Review = ReviewInfo.from_orm(body)
    try:
        with Session(engine) as session:
            session.add(Review)
            session.commit()
            session.refresh(Review)

        return True
    except IntegrityError:
        return False
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Intentional server error")
