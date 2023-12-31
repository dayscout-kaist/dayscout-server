from fastapi import APIRouter, HTTPException

router = APIRouter()

from src.schemas import Tag, TagCreateBody
from src.services import create_tag, remove_tag_by_id, search_all_tags


@router.get("/search/all")
async def search_all() -> list[Tag]:
    return search_all_tags()


@router.post("/create")
async def create(body: TagCreateBody) -> int:
    return create_tag(body)


@router.get("/remove")
async def remove(id: int) -> int:
    return remove_tag_by_id(id)
