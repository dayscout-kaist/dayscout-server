from fastapi import APIRouter

from src.schemas import Post, PostCreateBody
from src.services import create_post, search_post_by_food_id

router = APIRouter()


@router.post("/create")
async def create(body: PostCreateBody) -> bool:
    return create_post(body)


@router.get("/search/byFoodId")
async def search_by_food_id(id: int) -> list[Post]:
    return search_post_by_food_id(id)
