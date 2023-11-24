from typing import Optional

from src.utils.response import RequestModel


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
