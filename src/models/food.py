from datetime import datetime
from typing import List, Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from src.schemas.unit import FoodType, PrimaryUnit, UnitEnum


class FoodModel(SQLModel, table=True):
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


class ReportModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    food_id: int = Field(foreign_key="foodmodel.id")
    user_id: int = Field(foreign_key="usermodel.id")
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    reference: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    food: FoodModel = Relationship(back_populates="reports")
    # __table_args__ = (UniqueConstraint("food_id", "user_id"),)
