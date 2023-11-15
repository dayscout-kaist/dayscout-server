from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class PrimaryUnit(str, Enum):
    """
    기본 단위
    """

    g = "g"
    ml = "ml"


class FoodType(Enum):
    general = "general"
    distribution = "distribution"


class Standard_food(SQLModel, table=True):
    name: str = Field(default=None, primary_key=True)
    represent_name: str = Field(default=None)
    class_name: str = Field(default=None)
    total_weight: str = Field(default=None)
    per_unit: PrimaryUnit = Field(default="g")
    carbohydrate: Optional[float] = Field(default=None)
    protein: Optional[float] = Field(default=None)
    fat: Optional[float] = Field(default=None)
    sugar: Optional[float] = Field(default=None)
    energy: Optional[float] = Field(default=None)
    type: FoodType = Field(default="general")
