# services/user_service/app/infrastructure/models/user.py

import datetime

from service_server.app.infrastructure.db import Base
from sqlalchemy import TIMESTAMP, Column, String
from sqlalchemy.dialects.postgresql import UUID


class UserProfile(Base):
    __tablename__ = "user_profiles"


    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.UTC)