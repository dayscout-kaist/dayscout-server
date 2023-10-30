from fastapi import APIRouter

from src.services import get_auth_info

router = APIRouter()


@router.get("/")
async def info():
    return get_auth_info()


@router.post("/login")
async def login():
    return {}


@router.get("/logout")
async def logout():
    return {}


@router.post("/register")
async def logout():
    return {}
