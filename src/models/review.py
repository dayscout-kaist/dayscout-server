from typing import Optional

from sqlmodel import Field, SQLModel

from src.schemas.unit import FoodType, PrimaryUnit, UnitEnum


class ReviewModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    food_id: int = Field(default=None, foreign_key="foodmodel.id")
    author: str = Field(default=None)
    carbohydrate: Optional[float] = Field(default=None)
    protein: Optional[float] = Field(default=None)
    fat: Optional[float] = Field(default=None)
    sugar: Optional[float] = Field(default=None)
    energy: Optional[float] = Field(default=None)
    reference: int = Field(default=0)
    type: FoodType = Field()
