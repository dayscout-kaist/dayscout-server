from datetime import datetime

from fastapi import APIRouter, Depends, Query
from starlette.requests import Request

from src.schemas import CurrentUser, Post, PostCreateBody
from src.services import create_post, search_post_by_day, search_post_by_food_id
from src.utils.auth import get_authorized_user

router = APIRouter()


@router.post("/create")
async def create(
    body: PostCreateBody, current_user: CurrentUser = Depends(get_authorized_user)
) -> int:
    return create_post(body, current_user)


@router.get("/search/byFoodId")
async def search_by_food_id(id: int) -> list[Post]:
    return search_post_by_food_id(id)


@router.get("/search/byDay")
async def search_by_day(
    day: datetime = Query(None),
    current_user: CurrentUser = Depends(get_authorized_user),
) -> list[Post]:
    if day == None:
        day = datetime.today()
    return search_post_by_day(day, current_user)
