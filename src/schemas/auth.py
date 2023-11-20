from typing import Optional

from src.models import UserInfo
from src.utils.response import CamelModel


class UserInfoSession(CamelModel):
    id: int
    email: str
    username: str


class LoginBody(CamelModel):
    email: str
    password: str


class RegisterBody(CamelModel):
    email: str
    username: str
    password: str
    height: Optional[float]
    weight: Optional[float]
