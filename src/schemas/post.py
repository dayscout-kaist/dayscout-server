from datetime import datetime
from typing import Optional

from src.utils.response import RequestModel, ResponseModel

from .tag import Tag


class PostCreateBody(RequestModel):
    content: str
    food_id: int
    tag_ids: list[int] = []


class PostSearchByDayBody(RequestModel):
    datestr: Optional[str]


class Post(ResponseModel):
    id: int
    content: str
    food_id: int
    user_id: int
    tags: list[Tag] = []
    created_at: datetime
