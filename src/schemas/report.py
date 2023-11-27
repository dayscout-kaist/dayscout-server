from datetime import datetime
from typing import List, Optional

from src.utils.response import RequestModel, ResponseModel

from .food import Nutrients
from .unit import ConfirmEnum


class ReportReference(ResponseModel):
    id: int
    user_id: int
    confirm: ConfirmEnum
    created_at: datetime


class Report(ResponseModel):
    id: int
    food_id: int
    carbohydrate: Optional[float]
    protein: Optional[float]
    fat: Optional[float]
    sugar: Optional[float]
    energy: Optional[float]
    reference: int
    created_at: datetime
    references: List[ReportReference]


class ReportCreateBody(RequestModel):
    food_id: int
    nutrients: Nutrients


class ReportConfirmBody(RequestModel):
    report_id: int
    confirm: ConfirmEnum
