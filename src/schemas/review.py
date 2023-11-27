from src.utils.response import RequestModel

from .food import Nutrients


class ReviewCreateBody(RequestModel):
    food_id: int
    nutrients: Nutrients
