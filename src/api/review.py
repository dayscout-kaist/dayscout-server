from fastapi import APIRouter
from starlette.requests import Request

from src.schemas import ReviewCreateBody
from src.services import create_review
from src.utils.auth import getAuthorizedUserInfo

router = APIRouter()


@router.post("/create")
async def create(request: Request, body: ReviewCreateBody) -> int:
    userInfo = getAuthorizedUserInfo(request)
    return create_review(body, userInfo)
