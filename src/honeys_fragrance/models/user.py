from sqlalchemy import String, Column, TIMESTAMP, func, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

import uuid

from src.honeys_fragrance.db.base import Base


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    email_address = Column(String, index=True, nullable=False)
    telephone_number = Column(Integer, index=True, nullable=False)
    role = Column(String, server_default='user', nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    updated_at = Column(TIMESTAMP, nullable=True, default=func.now())

    user_addresses = relationship("UserAddress", back_populates="user")
