from uuid import UUID

from service_server.app.shared.infrastructure.model.base_model import BaseModel
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.enum.user.age_range import AgeRange
from common.enum.user.auth_channel import AuthChannel
from common.enum.user.gender import Gender


class UserModel(BaseModel):
    __tablename__ = "users"

    # 유저의 기본 필드
    nickname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=True)
    profile_image: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(nullable=True)
    gender: Mapped[Gender] = mapped_column(Enum(Gender), nullable=True)
    age_range: Mapped[AgeRange] = mapped_column(Enum(AgeRange), nullable=True)
    auth_channel: Mapped[AuthChannel] = mapped_column(Enum(AuthChannel), nullable=False)


    kakao: Mapped["KakaoModel"] = relationship("KakaoModel", back_populates="user") # type: ignore