from typing import Optional

from sqlmodel import Field, SQLModel


class ReviewModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    food_id: int = Field(foreign_key="foodmodel.id")
    user_id: int = Field(foreign_key="usermodel.id")
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    reference: int = Field(default=0)
    # type: FoodType = Field()
