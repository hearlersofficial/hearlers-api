import uuid
from datetime import datetime

from service_server.app.shared.infrastructure.model.base_model import BaseModel
from service_server.app.shared.infrastructure.model.user_model import UserModel
from service_server.app.user.domain.enum.age_range import AgeRange
from service_server.app.user.domain.enum.auth_channel import AuthChannel
from service_server.app.user.domain.enum.gender import Gender
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class KakaoModel(BaseModel):
    __tablename__ = "kakao"

    unique_id: Mapped[str] = mapped_column(nullable=False, comment="고유 아이디")
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False, comment="유저 ID")

    # Users와 OneToOne 관계
    user: Mapped[UserModel] = relationship("UserModel", back_populates="kakao")