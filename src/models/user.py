from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.schemas.unit import GenderEnum


class UserModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .report import UserReportModel
        from .review import ReviewModel

    id: int = Field(default=None, primary_key=True)
    username: str
    email: str = Field(unique=True)
    password: str
    height: Optional[float]
    weight: Optional[float]
    birth: Optional[str]
    gender: Optional[GenderEnum]

    user_reports: List["UserReportModel"] = Relationship(back_populates="user")
    reviews: List["ReviewModel"] = Relationship(back_populates="user")
