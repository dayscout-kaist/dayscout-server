from src.models import UserInfo
from src.utils.response import CamelModel


class UserInfoSession(CamelModel):
    id: UserInfo.__annotations__["id"]
    email: UserInfo.__annotations__["email"]
    username: UserInfo.__annotations__["username"]


class RegisterBody(CamelModel):
    email: UserInfo.__annotations__["email"]
    username: UserInfo.__annotations__["username"]
    password: UserInfo.__annotations__["password"]
    height: UserInfo.__annotations__["height"]
    weight: UserInfo.__annotations__["weight"]
