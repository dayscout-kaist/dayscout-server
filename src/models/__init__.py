from sqlmodel import Session, SQLModel, create_engine, select

from src.models import USERINFO
from src.schemas import UserCreate
from src.settings import settings

from .userInfo import *

DATABASE_URL = f"mysql+mysqldb://{settings.USER_NAME}:{settings.DB_PASSWORD}@{settings.HOST_NAME}/{settings.DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)
