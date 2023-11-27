from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

from src.schemas.unit import ConfirmEnum


class ReportModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .food import FoodModel

    id: int = Field(primary_key=True, default=None, index=True)
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    food_id: int = Field(foreign_key="foodmodel.id")
    food: "FoodModel" = Relationship(back_populates="reports")

    user_reports: List["UserReportModel"] = Relationship(back_populates="report")


class UserReportModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .user import UserModel

    id: int = Field(primary_key=True, default=None, index=True)
    confirm: ConfirmEnum = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    user_id: int = Field(foreign_key="usermodel.id")
    user: "UserModel" = Relationship(back_populates="user_reports")

    report_id: int = Field(foreign_key="reportmodel.id")
    report: "ReportModel" = Relationship(back_populates="user_reports")

    __table_args__ = (UniqueConstraint("user_id", "report_id"),)
