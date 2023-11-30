from datetime import datetime

from fastapi import APIRouter, Depends

from src.schemas import CurrentUser, Review, ReviewCreateBody, ReviewSearchByDayBody
from src.services import create_review, search_review_by_day, search_review_by_food_id
from src.utils.auth import get_authorized_user

router = APIRouter()


@router.post("/create")
async def create(
    body: ReviewCreateBody, current_user: CurrentUser = Depends(get_authorized_user)
) -> int:
    return create_review(body, current_user)


@router.get("/search/byFoodId")
async def search_by_food_id(id: int) -> list[Review]:
    return search_review_by_food_id(id)


@router.post("/search/byDay")
async def search_by_day(
    body: ReviewSearchByDayBody,
    current_user: CurrentUser = Depends(get_authorized_user),
) -> list[Review]:
    datestr = (
        datetime.today().strftime("%Y%m%d") if body.datestr == None else body.datestr
    )
    return search_review_by_day(datestr, current_user)
