import uuid
from datetime import datetime

from service_server.app.shared.infrastructure.db import Base
from sqlalchemy import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column


class BaseModel(Base):
    __abstract__ = True  # 이 클래스는 테이블로 생성되지 않음

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
