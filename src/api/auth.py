from typing import Union

from fastapi import APIRouter
from starlette.requests import Request

from src.schemas import RegisterBody, UserInfoSession
from src.services import register_user

router = APIRouter()


@router.get("/")
async def info(request: Request) -> Union[UserInfoSession, dict]:
    userInfo = request.session.get("userInfo")
    return {} if userInfo == None else userInfo


@router.post("/login")
async def login(request: Request):
    request.session["userInfo"] = None
    return {}


@router.get("/logout")
async def logout(request: Request) -> bool:
    userInfo = request.session.get("userInfo")
    if userInfo != None:
        request.session.clear()
        return True
    return False


@router.post("/register")
async def register(body: RegisterBody) -> bool:
    if register_user(body):
        return True
    return False
