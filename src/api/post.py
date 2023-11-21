from fastapi import APIRouter

from src.schemas import Post
from src.services import search_post_by_food_id

router = APIRouter()


@router.get("/search/byFoodId")
async def search_by_food_id(id: int) -> Post:
    return search_post_by_food_id(id)
