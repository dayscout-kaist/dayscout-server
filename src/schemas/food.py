from enum import Enum
from typing import Optional, Union

from src.utils.response import CamelModel

from .unit import AbsoluteUnit, PrimaryUnit, SingleUnit, TotalUnit


class Nutrients(CamelModel):
    carbohydrate: Optional[float] = None
    protein: Optional[float] = None
    fat: Optional[float] = None
    sugar: Optional[float] = None
    energy: Optional[float] = None


class FoodContent(CamelModel):
    total_weight: float
    unit: Union[AbsoluteUnit, TotalUnit, SingleUnit]
    primary_unit: PrimaryUnit
    nutrients: Nutrients


class FoodType(str, Enum):
    general = "general"
    distribution = "distribution"


class FoodInfo(CamelModel):
    name: str
    category: str
    manufacturer: Optional[str] = None
    content: FoodContent


class FoodContentOptional(FoodContent):
    total_weight: Optional[float]
    unit: Optional[Union[AbsoluteUnit, TotalUnit, SingleUnit]]
    primary_unit: Optional[PrimaryUnit]


class FoodName(CamelModel):
    name: str


class Food(CamelModel):
    name: str
    represent_name: str
    class_name: str
    total_weight: str
    per_unit: PrimaryUnit
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    type: FoodType
