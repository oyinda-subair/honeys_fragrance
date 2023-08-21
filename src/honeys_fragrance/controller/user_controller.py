
from datetime import datetime
from typing import Any, Dict, Optional, Union
from src.honeys_fragrance.controller.base import BaseController
from src.honeys_fragrance.core.utils import UserRole, get_password_hash
from src.honeys_fragrance.models import User
from src.honeys_fragrance.schemas import CreateUser, UpdateUser
from sqlalchemy.orm import Session


class UserController(BaseController[User, CreateUser, UpdateUser]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        user = db.query(User).filter(User.email == email).first()
        return user

    def create(self, db: Session, *, obj_in: CreateUser) -> User:
        create_data = obj_in.model_dump()
        create_data.pop("password")
        db_obj = User(**create_data)
        db_obj.hashed_password = get_password_hash(obj_in.password)
        db.add(db_obj)
        db.commit()

        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UpdateUser, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        update_data["updated_at"] = datetime.now()

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def is_admin(self, user: User) -> bool:
        return user.role == UserRole.ADMIN


user = UserController(User)
