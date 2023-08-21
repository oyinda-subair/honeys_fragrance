
import datetime
from pydantic import EmailStr

from src.honeys_fragrance.schemas.base import UserBase, UserInDBBase


class CreateUser(UserBase):
    first_name: str
    last_name: str
    email_address: EmailStr
    password: str
    telephone_number: int


class UpdateUser(UserBase):
    updated_at: datetime = datetime.now()


class UserInDB(UserInDBBase):
    hashed_password: str
