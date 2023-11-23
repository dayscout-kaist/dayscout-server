from typing import Optional

from sqlmodel import Field, SQLModel

from src.schemas.unit import FoodType, PrimaryUnit, UnitEnum


class FoodModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str = Field(default=None)
    represent_name: Optional[str] = Field(default=None)
    class_name: Optional[str] = Field(default=None)
    manufacturer: Optional[str] = Field(default=None)
    category: Optional[str] = Field(default=None)
    total_weight: float = Field(default=None)
    unit: UnitEnum = Field(default="absolute")
    primary_unit: PrimaryUnit = Field(default="g")
    carbohydrate: Optional[float] = Field(default=None)
    protein: Optional[float] = Field(default=None)
    fat: Optional[float] = Field(default=None)
    sugar: Optional[float] = Field(default=None)
    energy: Optional[float] = Field(default=None)
    type: FoodType = Field(default="general")
