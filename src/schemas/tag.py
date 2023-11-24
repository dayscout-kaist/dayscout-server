from src.utils.response import RequestModel


class TagInfo(RequestModel):
    id: int
    name: str


class TagCreateBody(RequestModel):
    name: str
