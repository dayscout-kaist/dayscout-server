from typing import Optional

from src.utils.response import RequestModel

from .unit import GenderEnum


class UserInfoSession(RequestModel):
    id: int
    email: str
    username: str


class LoginBody(RequestModel):
    email: str
    password: str


class RegisterBody(RequestModel):
    email: str
    username: str
    password: str
    height: Optional[float]
    weight: Optional[float]
    birth: Optional[str]
    gender: Optional[GenderEnum]
