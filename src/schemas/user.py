from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class User(UserBase):
    id: int


class UserCreate(UserBase):
    password: str
