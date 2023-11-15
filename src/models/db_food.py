from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class unit(Enum):
    g = ("g",)
    ml = "ml"


class Nutrients(SQLModel, table=True):
    name: str = Field(default=None)
    represent_name: str = Field(default=None)
    class_name: str = Field(default=None)
    total_weight: str = Field(default=None)
    per_unit: unit = Field(default="g")
    carbohydrate: Optional[float] = Field(default=None)
    protein: Optional[float] = Field(default=None)
    fat: Optional[float] = Field(default=None)
    sugar: Optional[float] = Field(default=None)
    energy: Optional[float] = Field(default=None)
