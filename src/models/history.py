from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel


class HistoryModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .food import FoodModel
        from .tag import HistoryTagModel
        from .user import UserModel

    id: int = Field(primary_key=True, default=None, index=True)
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    food_id: Optional[int] = Field(
        default=None, foreign_key="foodmodel.id", nullable=True
    )
    food: Optional["FoodModel"] = Relationship(back_populates="histories")

    user_id: int = Field(foreign_key="usermodel.id")
    user: "UserModel" = Relationship(back_populates="histories")

    post_content: Optional[str]
    post_created_at: Optional[datetime] = Field(
        default_factory=datetime.utcnow, nullable=False
    )
    post_tags: List["HistoryTagModel"] = Relationship(back_populates="history")
