from typing import Optional, Union

from src.utils.response import RequestModel, ResponseModel

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


class Nutrients(RequestModel):
    carbohydrate: Optional[float] = None
    protein: Optional[float] = None
    fat: Optional[float] = None
    sugar: Optional[float] = None
    energy: Optional[float] = None


class GeneralFoodContent(RequestModel):
    type = "general"
    total_weight: float
    unit: UnitEnum
    represent_name: Optional[str]
    class_name: Optional[str]
    primary_unit: PrimaryUnit = "g"
    nutrients: Nutrients
    original_nutrients: Nutrients


class DistributionFoodContent(RequestModel):
    type = "distribution"
    total_weight: float
    unit: UnitEnum
    manufacturer: Optional[str] = None
    represent_name: Optional[str]
    class_name: Optional[str]
    primary_unit: PrimaryUnit = "g"
    nutrients: Nutrients
    suggested_nutrients: Optional[Nutrients] = None


class FoodDetail(ResponseModel):
    id: int
    name: str
    tag: Optional[list[TagInfo]] = []
    content: Optional[Union[GeneralFoodContent, DistributionFoodContent]]
    image_src: Optional[str]


## 아래는 미정


class FoodContent(RequestModel):
    total_weight: float
    unit: Union[AbsoluteUnit, TotalUnit, SingleUnit]
    primary_unit: PrimaryUnit
    nutrients: Nutrients
    suggested_nutrients: Nutrients
    nutrients: Optional[Nutrients]
    original_nutrients: Optional[Nutrients]
    suggested_nutrients: Optional[Nutrients]


class FoodInfo(RequestModel):
    name: str
    # category: str
    manufacturer: Optional[str] = None
    content: FoodContent


class FoodContentOptional(FoodContent):
    total_weight: Optional[float]
    unit: Optional[Union[AbsoluteUnit, TotalUnit, SingleUnit]]
    primary_unit: Optional[PrimaryUnit]


class FoodCreateBody(RequestModel):
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
    img: Optional[str]


class FoodEditBody(RequestModel):
    food_id: int
    author: Optional[str]
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    type: FoodType = "general"


class FoodReportBody(RequestModel):
    food_id: int
    author: Optional[str]
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    reference: int
    type: FoodType = "distribution"


class ReportConfirmBody(RequestModel):
    food_id: int
    confirm: ConfirmEnum
