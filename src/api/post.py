from datetime import datetime

from fastapi import APIRouter, Query
from starlette.requests import Request

from src.schemas import Post, PostCreateBody
from src.services import create_post, search_post_by_day, search_post_by_food_id
from src.utils.auth import getAuthorizedUserInfo

router = APIRouter()


@router.post("/create")
async def create(request: Request, body: PostCreateBody) -> int:
    userInfo = getAuthorizedUserInfo(request)
    return create_post(body, userInfo)


@router.get("/search/byFoodId")
async def search_by_food_id(id: int) -> list[Post]:
    return search_post_by_food_id(id)


@router.get("/search/byDay")
async def search_by_day(request: Request, day: datetime = Query(None)) -> list[Post]:
    if day == None:
        day = datetime.today()
    userInfo = getAuthorizedUserInfo(request)
    return search_post_by_day(day, userInfo)
