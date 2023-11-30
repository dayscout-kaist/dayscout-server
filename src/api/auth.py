from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.schemas import CurrentUser, LoginBody, RegisterBody
from src.services import login_user, register_user
from src.utils.auth import get_authorized_user, oauth2_scheme

router = APIRouter()


@router.get("/")
async def info(current_user: CurrentUser = Depends(get_authorized_user)) -> CurrentUser:
    # userInfo = getAuthorizedUserInfo(request)
    return current_user


@router.post("/login")
async def login(body: LoginBody) -> CurrentUser:
    return login_user(body)


@router.post("/register")
async def register(body: RegisterBody) -> CurrentUser:
    return register_user(body)
