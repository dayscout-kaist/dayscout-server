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


class FoodInfo(CamelModel):
    name: str
    category: str
    manufacturer: Optional[str] = None
    content: FoodContent
