from enum import Enum
from typing import Literal

from pydantic import BaseModel


class AbsoluteUnit(BaseModel):
    """
    100g 당 영양 성분
    """

    type: Literal["absolute"] = "absolute"


class TotalUnit(BaseModel):
    """
    총 내용량 당 영양 성분
    """

    type: Literal["total"] = "total"
    totalWeight: float


class SingleUnit(BaseModel):
    """
    단위 섭취량 당 영양 성분
    """

    type: Literal["single"] = "single"
    unitName: str
    unitWeight: float


class PrimaryUnit(str, Enum):
    """
    기본 단위
    """

    g = "g"
    ml = "ml"
