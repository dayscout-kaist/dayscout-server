from typing import Optional

from src.utils.response import RequestModel, ResponseModel


class Tag(ResponseModel):
    id: int
    name: str
    color_background: Optional[str]
    color_border: Optional[str]


class TagCreateBody(RequestModel):
    name: str
    color_background: Optional[str]
    color_border: Optional[str]
