from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class TagModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str = Field(index=True, unique=True)
    color_background: Optional[str]
    color_border: Optional[str]

    # 관계 정의
    post_tags: List["PostTagModel"] = Relationship(back_populates="tag")


class PostModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    content: str = Field(default=None)
    food_id: int = Field(foreign_key="foodmodel.id")
    user_id: int = Field(foreign_key="usermodel.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # 관계 정의
    post_tags: List["PostTagModel"] = Relationship(back_populates="post")


class PostTagModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    post_id: int = Field(foreign_key="postmodel.id")
    tag_id: int = Field(foreign_key="tagmodel.id")

    # 관계 정의
    post: PostModel = Relationship(back_populates="post_tags")
    tag: TagModel = Relationship(back_populates="post_tags")
