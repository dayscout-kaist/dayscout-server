from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.schemas.unit import FoodType, PrimaryUnit, UnitEnum


class FoodModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .report import ReportModel
        from .review import ReviewModel

    id: int = Field(primary_key=True, default=None, index=True)
    name: str
    represent_name: Optional[str]
    class_name: Optional[str]
    manufacturer: Optional[str]
    total_weight: float
    unit: UnitEnum
    primary_unit: PrimaryUnit
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    type: FoodType
    image_src: Optional[str]
    barcode_number: Optional[str] = Field(index=True, unique=True)
    product_db_id: Optional[int] = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    reports: List["ReportModel"] = Relationship(back_populates="food")
    reviews: List["ReviewModel"] = Relationship(back_populates="food")
