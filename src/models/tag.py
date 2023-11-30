from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint


class TagModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str = Field(index=True, unique=True)
    color_background: Optional[str]
    color_border: Optional[str]

    review_tags: List["ReviewTagModel"] = Relationship(back_populates="tag")


class ReviewTagModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .review import ReviewModel

    id: int = Field(primary_key=True, default=None, index=True)

    review_id: int = Field(foreign_key="reviewmodel.id")
    review: "ReviewModel" = Relationship(back_populates="review_tags")

    tag_id: int = Field(foreign_key="tagmodel.id")
    tag: "TagModel" = Relationship(back_populates="review_tags")

    __table_args__ = (UniqueConstraint("review_id", "tag_id"),)
