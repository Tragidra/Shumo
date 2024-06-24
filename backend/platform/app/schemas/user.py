from typing import Optional
from pydantic import BaseModel, EmailStr, typing, Field, ConfigDict


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)
        metadata: typing.Dict[str, str] = Field(alias='metadata_')


class LoginForm(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
