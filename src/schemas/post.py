from datetime import datetime

from src.utils.response import CamelModel, ResponseModel


class PostCreateBody(CamelModel):
    content: str
    food_id: int
    user_id: int


class Post(ResponseModel):
    id: int
    content: str
    food_id: int
    user_id: int
    created_at: datetime
