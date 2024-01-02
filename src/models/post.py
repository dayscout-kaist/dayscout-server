from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel


class PostModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .history import HistoryModel
        from .tag import PostTagModel

    id: int = Field(primary_key=True, default=None, index=True)
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    history_id: int = Field(foreign_key="historymodel.id")
    history: "HistoryModel" = Relationship(back_populates="history")

    content: Optional[str]
    post_tags: List["PostTagModel"] = Relationship(back_populates="post")
