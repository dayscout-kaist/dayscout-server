from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel


class ReviewModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .food import FoodModel
        from .user import UserModel

    id: int = Field(primary_key=True, default=None, index=True)
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    food_id: int = Field(foreign_key="foodmodel.id")
    food: "FoodModel" = Relationship(back_populates="reviews")

    user_id: int = Field(foreign_key="usermodel.id")
    user: "UserModel" = Relationship(back_populates="reviews")
