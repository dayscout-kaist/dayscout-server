from fastapi import APIRouter
from starlette.requests import Request

from src.schemas import Post, PostCreateBody
from src.services import create_post, search_post_by_food_id
from src.utils.auth import getAuthorizedUserInfo

router = APIRouter()


@router.post("/create")
async def create(request: Request, body: PostCreateBody) -> int:
    userInfo = getAuthorizedUserInfo(request)
    return create_post(body, userInfo)


@router.get("/search/byFoodId")
async def search_by_food_id(id: int) -> list[Post]:
    return search_post_by_food_id(id)
