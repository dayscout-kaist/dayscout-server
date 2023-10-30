from typing import Optional

from sqlmodel import Field, SQLModel


class UserInfo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str
    height: Optional[float]
    weight: Optional[float]
