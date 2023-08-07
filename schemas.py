# Use this as a schema validator
from typing import List, Union

from pydantic import BaseModel


class UserIdBase(BaseModel):
    title: str


class UserIdCreate(UserIdBase):
    pass


class UserId(UserIdBase):
    id: int
    file_id: int

    class Config:
        orm_mode = True


class FileBase(BaseModel):
    filename: str


class FileCreate(FileBase):
    filename: str


class File(FileBase):
    id: int
    user_ids: List[UserId] = []

    class Config:
        orm_mode = True
