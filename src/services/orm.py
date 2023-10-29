from sqlmodel import Session, SQLModel, create_engine, select

from src.models import USERINFO
from src.schemas import UserCreate
from src.settings import settings

DATABASE_URL = f"mysql+mysqldb://{settings.USER_NAME}:{settings.DB_PASSWORD}@{settings.HOST_NAME}/{settings.DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)


def create_user_db(user: UserCreate) -> USERINFO:
    db_user = USERINFO.from_orm(user)
    with Session(engine) as session:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return db_user


def get_users_db(skip: int = 0, limit: int = 10) -> list:
    with Session(engine) as session:
        users = (
            session.execute(select(USERINFO).offset(skip).limit(limit)).scalars().all()
        )
    return users


def get_user_db(user_id: int) -> USERINFO:
    with Session(engine) as session:
        user = session.get(USERINFO, user_id)
    return user
