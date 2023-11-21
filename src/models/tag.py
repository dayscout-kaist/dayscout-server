from typing import Optional

from sqlmodel import Field, SQLModel


class TagInfo(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str = Field(default=None)
    colorBackground: Optional[str] = Field(default=None)
    colorBorder: Optional[str] = Field(default=None)
