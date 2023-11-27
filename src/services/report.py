from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from sqlmodel import Session, select

from src.models import ReportModel, UserReportModel, engine
from src.schemas import (
    Report,
    ReportConfirmBody,
    ReportCreateBody,
    ReportReference,
    UserInfoSession,
)


def create_report(body: ReportCreateBody, userInfo: UserInfoSession) -> Report:
    report = ReportModel(
        food_id=body.food_id,
        carbohydrate=body.nutrients.carbohydrate,
        protein=body.nutrients.protein,
        fat=body.nutrients.fat,
        sugar=body.nutrients.sugar,
        energy=body.nutrients.energy,
    )
    try:
        with Session(engine) as session:
            session.add(report)
            session.commit()
            session.refresh(report)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict")

    return confirm_report(ReportConfirmBody(reportId=report.id, confirm=1), userInfo)


def confirm_report(body: ReportConfirmBody, userInfo: UserInfoSession) -> Report:
    user_report = UserReportModel(
        user_id=userInfo["id"],
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

    if report is None:
        raise HTTPException(status_code=404, detail="Not Found")

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
