from src.utils.response import ResponseModel

from .food import Nutrients
from .unit import ConfirmEnum


class ReportCreateBody(ResponseModel):
    food_id: int
    nutrients: Nutrients


class ReportConfirmBody(ResponseModel):
    report_id: int
    confirm: ConfirmEnum
