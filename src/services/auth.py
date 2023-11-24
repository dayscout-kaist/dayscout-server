from bcrypt import checkpw, gensalt, hashpw
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from starlette.requests import Request

from src.models import UserModel, engine
from src.schemas import LoginBody, RegisterBody, UserInfoSession


def login_user(request: Request, body: LoginBody) -> bool:
    with Session(engine) as session:
        query = select(UserModel).where(UserModel.email == body.email)
        user = session.exec(query).first()

    if user == None:
        return False
    if not checkpw(body.password.encode("utf-8"), user.password.encode("utf-8")):
        return False

    request.session["userInfo"]: UserInfoSession = {
        "id": user.id,
        "email": user.email,
        "username": user.username,
    }
    return True


def register_user(body: RegisterBody) -> bool:
    try:
        body.password = hashpw(body.password.encode("utf-8"), gensalt()).decode("utf-8")
        user = UserModel.from_orm(body)
        with Session(engine) as session:
            session.add(user)
            session.commit()

    except IntegrityError:
        raise HTTPException(status_code=404, detail="Not Found")

    return True
