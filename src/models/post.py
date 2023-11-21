from datetime import datetime
from typing import List

from sqlmodel import JSON, Column, Field, SQLModel


class PostModel(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    content: str = Field(default=None)
    food_id: int = Field(default=None, foreign_key="userinfo.id")
    user_id: int = Field(default=None, foreign_key="foodinfo.id")
    tags: List[int] = Field(sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # Needed for Column(JSON)
    class Config:
        arbitrary_types_allowed = True
