from fastapi import APIRouter
from starlette.requests import Request

# from src.schemas import Report, ReportConfirmBody, ReportCreateBody
# from src.services import confirm_report, create_report
# from src.utils.auth import getAuthorizedUserInfo

router = APIRouter()


# @router.post("/create")
# async def create(request: Request, body: ReportCreateBody) -> Report:
#     userInfo = getAuthorizedUserInfo(request)
#     return create_report(body, userInfo)


# @router.post("/confirm")
# async def confirm(request: Request, body: ReportConfirmBody) -> Report:
#     userInfo = getAuthorizedUserInfo(request)
#     return confirm_report(body, userInfo)
