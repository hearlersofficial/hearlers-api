import datetime
import uuid

from service_server.app.infrastructure.db import Base
from sqlalchemy import TIMESTAMP, Column, String
from sqlalchemy.dialects.postgresql import UUID


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.UTC)