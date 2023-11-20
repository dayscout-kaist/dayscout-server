from fastapi import APIRouter, HTTPException

from src.schemas import ReviewCreateBody
from src.services import create_review

router = APIRouter()


@router.post("/create")
async def create(body: ReviewCreateBody) -> bool:
    if create_review(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")
