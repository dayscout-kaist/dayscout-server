from enum import Enum
from typing import Literal

from src.utils.response import CamelModel


class FoodType(str, Enum):
    general = "general"
    distribution = "distribution"


class AbsoluteUnit(CamelModel):
    """
    100g 당 영양 성분
    """

    type: Literal["absolute"] = "absolute"


class TotalUnit(CamelModel):
    """
    총 내용량 당 영양 성분
    """

    type: Literal["total"] = "total"


class SingleUnit(CamelModel):
    """
    단위 섭취량 당 영양 성분
    """

    type: Literal["single"] = "single"
    unit_name: str
    unit_weight: float


class PrimaryUnit(str, Enum):
    """
    기본 단위
    """

    g = "g"
    ml = "ml"
