from datetime import datetime

from src.utils.response import CamelModel


class Post(CamelModel):
    id: int
    content: str
    food_id: int
    user_id: int
    created_at: datetime
