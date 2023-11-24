from typing import Optional

from sqlmodel import Field, SQLModel


class TagModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str = Field(index=True, unique=True)
    color_background: Optional[str]
    color_border: Optional[str]
