from sqlalchemy import ForeignKey, String, Column, TIMESTAMP, func, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

import uuid

from src.honeys_fragrance.db.base import Base


class UserAddress(Base):
    __tablename__ = 'user_address'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id', ondelete='CASCADE'), index=True, nullable=False)
    address_line_1 = Column(String(256), nullable=False)
    address_line_2 = Column(String(256), nullable=True)
    city = Column(String, nullable=False)
    postal_code = Column(Integer, nullable=False)
    telephone_number = Column(Integer, nullable=False)
    mobile = Column(Integer, nullable=True)
    country = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    updated_at = Column(TIMESTAMP, nullable=True, default=func.now())

    user = relationship('User', back_populates='user_addresses')
