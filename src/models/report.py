from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel


class ReportModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .food import FoodModel

    id: int = Field(primary_key=True, default=None, index=True)
    user_id: int = Field(foreign_key="usermodel.id")
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    reference: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    food_id: int = Field(foreign_key="foodmodel.id")
    food: "FoodModel" = Relationship(back_populates="reports")

    # __table_args__ = (UniqueConstraint("food_id", "user_id"),)
