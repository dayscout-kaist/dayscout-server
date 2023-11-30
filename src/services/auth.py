from bcrypt import checkpw, gensalt, hashpw
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from starlette.requests import Request

from src.models import UserModel, engine
from src.schemas import CurrentUser, LoginBody, RegisterBody
from src.utils.auth import create_access_token, get_authorized_user


def login_user(body: LoginBody) -> CurrentUser:
    with Session(engine) as session:
        query = select(UserModel).where(UserModel.email == body.email)
        user = session.exec(query).first()

    if user == None:
        raise HTTPException(status_code=400, detail="Bad Request")
    if not checkpw(body.password.encode("utf-8"), user.password.encode("utf-8")):
        raise HTTPException(status_code=400, detail="Bad Request")

    token = create_access_token(
        {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "height": user.height,
            "weight": user.weight,
            "birth": user.birth,
            "gender": user.gender,
        }
    )
    return get_authorized_user(token)


def register_user(body: RegisterBody) -> CurrentUser:
    try:
        body.password = hashpw(body.password.encode("utf-8"), gensalt()).decode("utf-8")
        user = UserModel.from_orm(body)
        with Session(engine) as session:
            session.add(user)
            session.commit()

    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict")

    return login_user(
        LoginBody(
            email=user.email,
            password=user.password,
        )
    )
