from typing import Optional

from sqlmodel import Field, SQLModel

from src.schemas.food import FoodType
from src.schemas.unit import PrimaryUnit


class Food(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str = Field(default=None)
    represent_name: Optional[str] = Field(default=None)
    class_name: Optional[str] = Field(default=None)
    total_weight: float = Field(default=None)
    per_unit: PrimaryUnit = Field(default="g")
    manufacturer: Optional[str] = Field(default=None)
    original_carbohydrate: Optional[float] = Field(default=None)
    original_protein: Optional[float] = Field(default=None)
    original_fat: Optional[float] = Field(default=None)
    original_sugar: Optional[float] = Field(default=None)
    original_energy: Optional[float] = Field(default=None)
    type: FoodType = Field(default="general")
