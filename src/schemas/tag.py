from src.utils.response import CamelModel


class TagInfo(CamelModel):
    id: int
    name: str


class TagCreateBody(CamelModel):
    name: str
