from fastapi import APIRouter, Depends

from src.schemas import CurrentUser, Report, ReportConfirmBody, ReportCreateBody
from src.services import confirm_report, create_report
from src.utils.auth import get_authorized_user

router = APIRouter()


@router.post("/create")
async def create(
    body: ReportCreateBody, current_user: CurrentUser = Depends(get_authorized_user)
) -> Report:
    return create_report(body, current_user)


@router.post("/confirm")
async def confirm(
    body: ReportConfirmBody, current_user: CurrentUser = Depends(get_authorized_user)
) -> Report:
    return confirm_report(body, current_user)
