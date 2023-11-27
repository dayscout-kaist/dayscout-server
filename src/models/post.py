from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlmodel import Field, Relationship, SQLModel


class PostModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    content: str = Field(default=None)
    food_id: int = Field(foreign_key="foodmodel.id")
    user_id: int = Field(foreign_key="usermodel.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    if TYPE_CHECKING:
        from .tag import PostTagModel
    post_tags: List["PostTagModel"] = Relationship(back_populates="post")
