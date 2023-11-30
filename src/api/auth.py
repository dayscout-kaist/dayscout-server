from fastapi import APIRouter, Depends

from src.schemas import CurrentUser, LoginBody, RegisterBody
from src.services import login_user, register_user
from src.utils.auth import get_authorized_user

router = APIRouter()


@router.post("/")
async def info(current_user: CurrentUser = Depends(get_authorized_user)) -> CurrentUser:
    return current_user


@router.post("/login")
async def login(body: LoginBody) -> CurrentUser:
    return login_user(body)


# @router.post("/token")
# async def token(body: LoginBody):
#     return login_token(body)


@router.post("/register")
async def register(body: RegisterBody) -> CurrentUser:
    return register_user(body)
