import datetime
from typing import Optional
import uuid
from pydantic import EmailStr

from src.honeys_fragrance.schemas.base import CamelModel, UserBase, UserInDBBase


class UserAddressBase(CamelModel):
    address_line_1: Optional[str]
    address_line_2: Optional[str]
    city: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
    telephone_number: Optional[int] = None
    mobile: Optional[int] = None


class UserAddressInDBBase(UserAddressBase):
    id: uuid.UUID
    user_id: uuid.UUID

    class Config:
        orm_mode = True


class CreateUserAddress(UserAddressBase):
    address_line_1: str
    city: str
    country: str
    postal_code: str
    telephone_number: int


class UpdateUserAddress(UserAddressBase):
    updated_at: datetime = datetime.now()
