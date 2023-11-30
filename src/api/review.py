from fastapi import APIRouter, Depends

from src.schemas import CurrentUser, ReviewCreateBody
from src.services import create_review
from src.utils.auth import get_authorized_user

router = APIRouter()


@router.post("/create")
async def create(
    body: ReviewCreateBody, current_user: CurrentUser = Depends(get_authorized_user)
) -> int:
    return create_review(body, current_user)
