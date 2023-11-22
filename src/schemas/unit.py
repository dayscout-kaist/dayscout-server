from enum import Enum
from typing import Literal

from src.utils.response import RequestModel


class FoodType(str, Enum):
    general = "general"
    distribution = "distribution"


class AbsoluteUnit(RequestModel):
    """
    100g 당 영양 성분
    """

    type: Literal["absolute"] = "absolute"


class TotalUnit(RequestModel):
    """
    총 내용량 당 영양 성분
    """

    type: Literal["total"] = "total"


class SingleUnit(RequestModel):
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


class UnitEnum(str, Enum):
    absolulteUnit = "absolute"
    totalUnit = "total"
    singleUnit = "single"
