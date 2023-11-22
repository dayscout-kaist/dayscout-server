from fastapi import APIRouter, HTTPException

from src.schemas import EditCreateBody
from src.services import create_edit

router = APIRouter()


@router.post("/create")
async def create(body: EditCreateBody) -> bool:
    if create_edit(body):
        return True
    raise HTTPException(status_code=409, detail="Conflict")
