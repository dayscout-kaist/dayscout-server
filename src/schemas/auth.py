from typing import Optional

from src.utils.response import RequestModel, ResponseModel

from .unit import GenderEnum


class CurrentUser(ResponseModel):
    token: Optional[str]
    id: int
    email: str
    username: str
    height: Optional[float]
    weight: Optional[float]
    birth: Optional[str]
    gender: Optional[GenderEnum]


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
