from fastapi import HTTPException
from starlette.requests import Request


def getAuthorizedUserInfo(request: Request):
    userInfo = request.session.get("userInfo")
    if userInfo == None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return userInfo
