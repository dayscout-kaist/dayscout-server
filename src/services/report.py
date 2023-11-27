from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from src.models import FoodModel, ReviewModel, engine
from src.schemas import ReportConfirmBody, ReportCreateBody, UserInfoSession


def create_report(body: ReportCreateBody, userInfo: UserInfoSession):
    report = ReviewModel.from_orm(body)
    try:
        with Session(engine) as session:
            session.add(report)
            session.commit()
            session.refresh(report)

    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict")

    return report.id


def confirm_report(body: ReportConfirmBody):
    try:
        with Session(engine) as session:
            review = session.query(ReviewModel).filter_by(food_id=body.food_id).first()
            print("review", review)
            if review is not None:
                print("body confirm", body.confirm)
                review.reference = review.reference + body.confirm
            if review.reference >= 3:
                food = session.query(FoodModel).filter_by(id=body.food_id).first()
                if food:
                    # ReviewModel의 정보로 업데이트
                    food.carbohydrate = review.carbohydrate
                    food.fat = review.fat
                    food.protein = review.protein
                    food.sugar = review.sugar
                    food.energy = review.energy
                    session.delete(review)
                else:
                    raise HTTPException(status_code=404, detail="Food not found")
            elif review.reference <= -3:
                session.delete(review)

            session.commit()

            session.close()

        return True
    except IntegrityError:
        return False
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Intentional server error")
