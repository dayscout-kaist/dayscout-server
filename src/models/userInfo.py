from typing import Optional

from sqlmodel import Field, SQLModel


class UserInfo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    height: Optional[float]
    weight: Optional[float]
