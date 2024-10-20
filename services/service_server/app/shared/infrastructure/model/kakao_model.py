from uuid import UUID

from service_server.app.shared.infrastructure.model.base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class KakaoModel(BaseModel):
    __tablename__ = "kakao"

    # 고유 아이디 필드
    unique_id: Mapped[str] = mapped_column(nullable=False, comment="고유 아이디")
    
    # UserModel과의 외래 키 연결 (users 테이블의 id를 참조)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False, comment="유저 ID")

    user: Mapped["UserModel"] = relationship("UserModel", back_populates="kakao") # type: ignore
