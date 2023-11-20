from sqlmodel import Field, SQLModel


class TagInfo(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None, index=True)
    name: str = Field(default=None)
