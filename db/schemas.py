from typing import Union
from pydantic import BaseModel


class ImageBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ImageCreate(BaseModel):
    pass


class Image(BaseModel):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    user_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    image: list[Image] = []

    class Config:
        orm_model = True

