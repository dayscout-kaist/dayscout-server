from typing import Optional

from sqlmodel import Field, SQLModel


class TagModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str = Field(default=None)
    color_background: Optional[str] = Field(default=None)
    color_border: Optional[str] = Field(default=None)
