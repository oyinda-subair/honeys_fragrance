
from datetime import datetime
from typing import Any, Dict, Union
from src.honeys_fragrance.controller.base import BaseController
from src.honeys_fragrance.models import User
from src.honeys_fragrance.models import UserAddress
from sqlalchemy.orm import Session

from src.honeys_fragrance.schemas import CreateUserAddress, UpdateUserAddress


class UserAddressController(BaseController[UserAddress, CreateUserAddress, UpdateUserAddress]):

    def update(
        self, db: Session, *, db_obj: UserAddress, obj_in: Union[UpdateUserAddress, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        update_data["updated_at"] = datetime.now()

        return super().update(db, db_obj=db_obj, obj_in=update_data)


user = UserAddressController(UserAddress)
