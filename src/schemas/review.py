from datetime import datetime
from typing import Optional

from src.utils.response import RequestModel, ResponseModel

from .food import Nutrients
from .tag import Tag


class ReviewCreateBody(RequestModel):
    food_id: int
    nutrients: Nutrients
    content: str
    tag_ids: list[int] = []


class ReviewSearchByDayBody(RequestModel):
    datestr: Optional[str]


class Review(ResponseModel):
    id: int
    content: str
    food_id: int
    user_id: int
    nutrients: Nutrients
    tags: list[Tag] = []
    created_at: datetime
