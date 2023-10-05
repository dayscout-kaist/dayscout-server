from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TextBody(BaseModel):
    text: str = ""


class PrimaryUnit(Enum):
    g = "g"
    ml = "ml"


class UnitType(Enum):
    absolute = "absolute"
    total = "total"
    single = "single"


class Unit(BaseModel):
    type: UnitType
    totalWeight: Optional[float] = None
    unitName: Optional[str] = None
    unitWeight: Optional[float] = None


class Nutrients(BaseModel):
    fat: Optional[float] = None
    carbohydrate: Optional[float] = None
    sugar: Optional[float] = None
    energy: Optional[float] = None
    protein: Optional[float] = None


class FoodContent(BaseModel):
    totalWeight: Optional[float] = None
    unit: Unit
    primaryUnit: PrimaryUnit
    nutrients: Nutrients


class FoodInfo(BaseModel):
    name: str
    category: str
    manufacturer: Optional[str] = None
    content: FoodContent
