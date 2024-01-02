from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint


class TagModel(SQLModel, table=True):
    id: str = Field(primary_key=True, index=True, unique=True)
    name: str = Field(unique=True)

    post_tags: List["PostTagModel"] = Relationship(back_populates="tag")


class PostTagModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .post import PostModel

    id: int = Field(primary_key=True, default=None, index=True)

    post_id: int = Field(foreign_key="postmodel.id")
    post: "PostModel" = Relationship(back_populates="post_tags")

    tag_id: str = Field(foreign_key="tagmodel.id")
    tag: "TagModel" = Relationship(back_populates="post_tags")

    __table_args__ = (UniqueConstraint("post_id", "tag_id"),)
