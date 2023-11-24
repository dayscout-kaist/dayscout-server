from sqlmodel import SQLModel, create_engine

from src.settings import settings

from .edit import *
from .food import *
from .post import *
from .tag import *
from .user import *

DATABASE_URL = f"mysql+mysqldb://{settings.MYSQL_USER_NAME}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}/{settings.MYSQL_DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)
