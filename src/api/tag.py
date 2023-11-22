from fastapi import APIRouter, HTTPException

router = APIRouter()

from src.schemas import TagCreateBody, TagInfo
from src.services import create_tag, remove_tag_by_id, search_all_tags


@router.get("/search/all")
async def search_all() -> list[TagInfo]:
    return search_all_tags()


@router.post("/create")
async def create(body: TagCreateBody) -> bool:
    if create_tag(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")


@router.get("/remove")
async def remove(id: int) -> bool:
    if remove_tag_by_id(id):
        return True
    raise HTTPException(status_code=404, detail="Not Found")
