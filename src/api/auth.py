from fastapi import APIRouter
from starlette.requests import Request

from src.schemas import LoginBody, RegisterBody, UserInfoSession
from src.services import login_user, register_user
from src.utils.auth import getAuthorizedUserInfo

router = APIRouter()


@router.get("/")
async def info(request: Request) -> UserInfoSession:
    userInfo = getAuthorizedUserInfo(request)
    return userInfo


@router.post("/login")
async def login(request: Request, body: LoginBody) -> bool:
    return login_user(request, body)


@router.get("/logout")
async def logout(request: Request) -> bool:
    request.session.clear()
    return True


@router.post("/register")
async def register(body: RegisterBody) -> bool:
    return register_user(body)
