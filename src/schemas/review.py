# from datetime import datetime
# from typing import List, Optional

from src.utils.response import RequestModel, ResponseModel

from .food import Nutrients


class ReviewCreateBody(RequestModel):
    food_id: int
    nutrients: Nutrients
