from typing import Optional, Union

from src.utils.response import RequestModel, ResponseModel

from .tag import Tag
from .unit import (
    AbsoluteUnit,
    ConfirmEnum,
    FoodType,
    PrimaryUnit,
    SingleUnit,
    TotalUnit,
    UnitEnum,
)


class Nutrients(ResponseModel):
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]


class GeneralFoodContent(ResponseModel):
    type = "general"
    total_weight: float
    unit: UnitEnum
    represent_name: Optional[str]
    class_name: Optional[str]
    primary_unit: PrimaryUnit = "g"
    nutrients: Nutrients
    original_nutrients: Nutrients


class DistributionFoodContent(ResponseModel):
    type = "distribution"
    total_weight: float
    unit: UnitEnum
    manufacturer: Optional[str]
    represent_name: Optional[str]
    class_name: Optional[str]
    primary_unit: PrimaryUnit = "g"
    nutrients: Nutrients
    suggested_nutrients: Optional[Nutrients]


class FoodDetail(ResponseModel):
    id: int
    name: str
    tag: list[Tag]
    content: Union[GeneralFoodContent, DistributionFoodContent]
    image_src: Optional[str]


class Food(ResponseModel):
    id: int
    name: str
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
    image_src: Optional[str]
    barcode_number: Optional[str]


class FoodEditBody(RequestModel):
    food_id: int
    author: Optional[str]
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    type: FoodType = "general"
