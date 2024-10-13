import uuid
from datetime import datetime

from service_server.app.shared.infrastructure.model.base_model import BaseModel
from service_server.app.shared.infrastructure.model.user_model import UserModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.enum.user.age_range import AgeRange
from common.enum.user.auth_channel import AuthChannel
from common.enum.user.gender import Gender


class KakaoModel(BaseModel):
    __tablename__ = "kakao"

    unique_id: Mapped[str] = mapped_column(nullable=False, comment="고유 아이디")
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False, comment="유저 ID")

    # Users와 OneToOne 관계
    user: Mapped[UserModel] = relationship("UserModel", back_populates="kakao")