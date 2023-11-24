from datetime import datetime

from src.utils.response import RequestModel, ResponseModel


class PostCreateBody(RequestModel):
    content: str
    food_id: int
    tag_ids: list[int] = []


class Post(ResponseModel):
    id: int
    content: str
    food_id: int
    user_id: int
    created_at: datetime
