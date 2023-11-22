from typing import Optional, Union

from src.utils.response import CamelModel

from .tag import TagInfo
from .unit import FoodType


class EditCreateBody(CamelModel):
    food_info_id: int
    author: Optional[str]
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    type: FoodType = "general"
