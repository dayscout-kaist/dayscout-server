from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel


class ReviewModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .food import FoodModel
        from .tag import ReviewTagModel
        from .user import UserModel

    id: int = Field(primary_key=True, default=None, index=True)
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    content: Optional[str]

    food_id: Optional[int] = Field(
        default=None, foreign_key="foodmodel.id", nullable=True
    )
    food: "FoodModel" = Relationship(back_populates="reviews")

    user_id: int = Field(foreign_key="usermodel.id")
    user: "UserModel" = Relationship(back_populates="reviews")

    review_tags: List["ReviewTagModel"] = Relationship(back_populates="review")
