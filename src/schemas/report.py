from src.utils.response import ResponseModel

from .food import Nutrients
from .unit import ConfirmEnum, FoodType


class ReportCreateBody(ResponseModel):
    food_id: int
    nutrients: Nutrients
    reference: int
    type: FoodType = "distribution"


class ReportConfirmBody(ResponseModel):
    food_id: int
    confirm: ConfirmEnum
