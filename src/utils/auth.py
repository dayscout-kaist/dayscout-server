from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request

from src.schemas import CurrentUser, TokenBody
from src.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=120)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def get_authorized_user(body: TokenBody) -> CurrentUser:
    try:
        userInfo = jwt.decode(body.token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if userInfo.get("id") == None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return CurrentUser(
        token=body.token,
        id=userInfo.get("id"),
        email=userInfo.get("email"),
        username=userInfo.get("username"),
        height=userInfo.get("height"),
        weight=userInfo.get("weight"),
        birth=userInfo.get("birth"),
        gender=userInfo.get("gender"),
    )


def getAuthorizedUserInfo(request: Request):
    userInfo = request.session.get("userInfo")
    if userInfo == None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return userInfo
