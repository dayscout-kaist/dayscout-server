from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.schemas.unit import FoodType, PrimaryUnit, UnitEnum


class FoodModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .history import HistoryModel
        from .report import ReportModel

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
    image_src: Optional[str] = Field(max_length=500)
    barcode_number: Optional[str] = Field(index=True, unique=True)
    product_db_id: Optional[int] = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    reports: List["ReportModel"] = Relationship(back_populates="food")
    histories: List["HistoryModel"] = Relationship(back_populates="food")
