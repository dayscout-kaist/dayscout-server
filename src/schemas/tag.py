from typing import Optional

from src.utils.response import RequestModel


class TagInfo(RequestModel):
    id: int
    name: str


class TagCreateBody(RequestModel):
    name: str
    color_background: Optional[str]
    color_border: Optional[str]
