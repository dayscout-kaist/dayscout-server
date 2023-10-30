from bcrypt import gensalt, hashpw
from sqlmodel import Session

from src.models import UserInfo, engine
from src.schemas import RegisterBody


def register_user(body: RegisterBody):
    body.password = hashpw(body.password.encode("utf-8"), gensalt()).decode("utf-8")
    user = UserInfo.from_orm(body)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return True
