from typing import Optional, Union

from pydantic import BaseModel

from src.utils.response import CamelModel

from .tag import TagInfo
from .unit import (
    AbsoluteUnit,
    ConfirmEnum,
    FoodType,
    PrimaryUnit,
    SingleUnit,
    TotalUnit,
    UnitEnum,
)


class Nutrients(CamelModel):
    carbohydrate: Optional[float] = None
    protein: Optional[float] = None
    fat: Optional[float] = None
    sugar: Optional[float] = None
    energy: Optional[float] = None


class GeneralFoodContent(CamelModel):
    type = "general"
    total_weight: float
    unit: AbsoluteUnit
    primary_unit: PrimaryUnit = "g"
    nutrients: Nutrients
    original_nutrients: Nutrients


class DistributionFoodContent(CamelModel):
    type = "distribution"
    total_weight: float
    manufacturer: Optional[str] = None
    category: str
    nutrients: Nutrients
    suggested_nutrients: Optional[Nutrients] = None


class FoodDetail(BaseModel):
    id: int
    name: str
    tag: Optional[list[TagInfo]] = []
    content: Optional[Union[GeneralFoodContent, DistributionFoodContent]]


## 아래는 미정


class FoodContent(CamelModel):
    total_weight: float
    unit: Union[AbsoluteUnit, TotalUnit, SingleUnit]
    primary_unit: PrimaryUnit
    nutrients: Nutrients
    suggested_nutrients: Nutrients
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


class FoodCreateBody(CamelModel):
    name: str
    represent_name: Optional[str]
    class_name: Optional[str]
    manufacturer: Optional[str]
    total_weight: float
    unit: UnitEnum
    primary_unit: PrimaryUnit = "g"
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    type: FoodType = "general"


class FoodEditBody(CamelModel):
    food_id: int
    author: Optional[str]
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    type: FoodType = "general"


class FoodReportBody(CamelModel):
    food_id: int
    author: Optional[str]
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    reference: int
    type: FoodType = "distribution"


class ReportConfirmBody(CamelModel):
    food_id: int
    confirm: ConfirmEnum
