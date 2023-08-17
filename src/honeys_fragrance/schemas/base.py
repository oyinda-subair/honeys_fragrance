from typing import Optional
import uuid
from pydantic import BaseModel, EmailStr
from humps import camelize

from src.honeys_fragrance.schemas.utils import UserRole


def to_camel(string):
    return camelize(string)


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class UserBase(CamelModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[EmailStr] = None
    telephone_numbe: Optional[int] = None
    role: Optional[UserRole] = UserRole.USER


class UserInDBBase(UserBase):
    id: uuid.UUID

    class Config:
        orm_mode = True
