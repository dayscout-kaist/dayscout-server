from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from sqlmodel import Session, select

from src.models import FoodModel, ReportModel, UserReportModel, engine
from src.schemas import (
    CurrentUser,
    Report,
    ReportConfirmBody,
    ReportCreateBody,
    ReportReference,
)

# report confirm이 3번 이상 확인되면 자동으로 반영
confirm_threshold = 3


def create_report(body: ReportCreateBody, current_user: CurrentUser) -> Report:
    report = ReportModel(
        food_id=body.food_id,
        carbohydrate=body.nutrients.carbohydrate,
        protein=body.nutrients.protein,
        fat=body.nutrients.fat,
        sugar=body.nutrients.sugar,
        energy=body.nutrients.energy,
        is_valid=True,
    )
    try:
        with Session(engine) as session:
            session.add(report)
            session.commit()
            session.refresh(report)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict")

    return confirm_report(
        ReportConfirmBody(reportId=report.id, confirm=1), current_user
    )


def confirm_report(body: ReportConfirmBody, current_user: CurrentUser) -> Report:
    user_report = UserReportModel(
        user_id=current_user.id,
        report_id=body.report_id,
        confirm=body.confirm,
    )
    try:
        with Session(engine) as session:
            session.add(user_report)
            session.commit()
            session.refresh(user_report)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict")

    with Session(engine) as session:
        report = session.exec(
            select(ReportModel)
            .where(ReportModel.id == user_report.report_id)
            .options(joinedload(ReportModel.user_reports))
        ).first()

        if report == None or report.is_valid == False:
            raise HTTPException(status_code=404, detail="Not Found")

        sum_confirm = sum([user_report.confirm for user_report in report.user_reports])
        if sum_confirm >= confirm_threshold:
            food = session.query(FoodModel).filter_by(id=body.food_id).first()

            if food is None:
                raise HTTPException(status_code=404, detail="Not Found")

            if report.carbohydrate is not None:
                food.carbohydrate = report.carbohydrate
            if report.protein is not None:
                food.protein = report.protein
            if report.fat is not None:
                food.fat = report.fat
            if report.sugar is not None:
                food.sugar = report.sugar
            if report.energy is not None:
                food.energy = report.energy

            report.is_valid = False
            session.commit()
            session.refresh(report)

        elif sum_confirm <= -confirm_threshold:
            report.is_valid = False
            session.commit()
            session.refresh(report)

    return Report(
        id=report.id,
        food_id=report.food_id,
        carbohydrate=report.carbohydrate,
        protein=report.protein,
        fat=report.fat,
        sugar=report.sugar,
        energy=report.energy,
        reference=user_report.id,
        created_at=report.created_at,
        sum_confirm=sum_confirm,
        references=[
            ReportReference(
                id=user_report.id,
                user_id=user_report.user_id,
                confirm=user_report.confirm,
                created_at=user_report.created_at,
            )
            for user_report in report.user_reports
        ],
    )
