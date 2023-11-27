from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from src.schemas import FoodReportBody, ReportConfirmBody
from src.services import confirm_report, create_report
from src.utils.auth import getAuthorizedUserInfo

router = APIRouter()


@router.post("/create")
async def create(request: Request, body: FoodReportBody) -> int:
    userInfo = getAuthorizedUserInfo(request)
    return create_report(body, userInfo)


@router.post("/confirm")
async def confirm(body: ReportConfirmBody) -> bool:
    if confirm_report(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")
