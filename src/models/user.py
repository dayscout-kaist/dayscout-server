from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel


class UserModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .report import UserReportModel

    id: int = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str
    height: Optional[float]
    weight: Optional[float]

    user_reports: List["UserReportModel"] = Relationship(back_populates="user")
