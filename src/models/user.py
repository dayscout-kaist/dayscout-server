from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.schemas.unit import GenderEnum


class UserModel(SQLModel, table=True):
    if TYPE_CHECKING:
        from .history import HistoryModel
        from .report import UserReportModel

    id: int = Field(default=None, index=True, primary_key=True)
    nickname: str
    email: str = Field(unique=True)
    password: str
    height: Optional[float]
    weight: Optional[float]
    birth: Optional[datetime]
    gender: Optional[GenderEnum]
    signup_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    user_reports: List["UserReportModel"] = Relationship(back_populates="user")
    histories: List["HistoryModel"] = Relationship(back_populates="user")
    devices: List["DeviceModel"] = Relationship(back_populates="user")


class DeviceModel(SQLModel, table=True):
    token: str = Field(primary_key=True, index=True)
    notification_after_one_hour: bool = Field(default=False)
    notification_after_two_hours: bool = Field(default=False)
    notification_after_four_hours: bool = Field(default=False)

    user_id: int = Field(foreign_key="usermodel.id")
    user: "UserModel" = Relationship(back_populates="devices")
