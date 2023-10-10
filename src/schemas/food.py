from typing import Optional, Union

from pydantic import BaseModel

from .unit import AbsoluteUnit, PrimaryUnit, SingleUnit, TotalUnit


class Nutrients(BaseModel):
    carbohydrate: Optional[float] = None
    protein: Optional[float] = None
    fat: Optional[float] = None
    sugar: Optional[float] = None
    energy: Optional[float] = None


class FoodContent(BaseModel):
    totalWeight: float
    unit: Union[AbsoluteUnit, TotalUnit, SingleUnit]
    primaryUnit: PrimaryUnit
    nutrients: Nutrients


class FoodInfo(BaseModel):
    name: str
    category: str
    manufacturer: Optional[str] = None
    content: FoodContent
