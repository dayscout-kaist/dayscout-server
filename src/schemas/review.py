from typing import Optional, Union

from src.utils.response import CamelModel

from .tag import TagInfo
from .unit import AbsoluteUnit, FoodType, PrimaryUnit, SingleUnit, TotalUnit, UnitEnum


class ReviewCreateBody(CamelModel):
    foodInfoId: int
    author: Optional[str]
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    type: FoodType = "general"
