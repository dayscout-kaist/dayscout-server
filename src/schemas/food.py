from enum import Enum
from typing import Optional, Union

from src.utils.response import CamelModel

from .unit import AbsoluteUnit, PrimaryUnit, SingleUnit, TotalUnit


class FoodType(str, Enum):
    general = "general"
    distribution = "distribution"


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
    nutrients: Optional[Nutrients]
    original_nutrients: Optional[Nutrients]
    suggested_nutrients: Optional[Nutrients]


class FoodInfo(CamelModel):
    name: str
    # category: str
    manufacturer: Optional[str] = None
    content: FoodContent


class FoodContentOptional(FoodContent):
    total_weight: Optional[float]
    unit: Optional[Union[AbsoluteUnit, TotalUnit, SingleUnit]]
    primary_unit: Optional[PrimaryUnit]


class Food(CamelModel):
    id: int
    name: str
    represent_name: Optional[str]
    class_name: Optional[str]
    total_weight: str
    per_unit: PrimaryUnit
    manufacturer: Optional[str] = None
    original_carbohydrate: Optional[float]
    original_protein: Optional[float]
    original_fat: Optional[float]
    original_sugar: Optional[float]
    original_energy: Optional[float]
    type: FoodType
    # food_info: FoodInfo
