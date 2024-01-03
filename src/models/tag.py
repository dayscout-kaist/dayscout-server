from typing import TYPE_CHECKING, List

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint


class TagModel(SQLModel, table=True):
    id: str = Field(primary_key=True, index=True, unique=True)
    name: str = Field(unique=True)

    post_tags: List["HistoryTagModel"] = Relationship(back_populates="tag")


class HistoryTagModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .history import HistoryModel

    id: int = Field(primary_key=True, default=None, index=True)

    history_id: int = Field(foreign_key="historymodel.id")
    history: "HistoryModel" = Relationship(back_populates="post_tags")

    tag_id: str = Field(foreign_key="tagmodel.id")
    tag: "TagModel" = Relationship(back_populates="post_tags")

    __table_args__ = (UniqueConstraint("history_id", "tag_id"),)
