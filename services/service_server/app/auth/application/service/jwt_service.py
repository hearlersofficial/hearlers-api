from service_server.app.shared.infrastructure.model.auth_user import \
    AuthUserModel
from sqlalchemy.orm import Session

from common.service.jwt_service import JWTService


class JWTServiceWithDB(JWTService):
    def __init__(self, db: Session):
        self.db = db
# Auth -> User도메인으로 합칠까? 나쁘지 않을듯
    def is_refresh_token_valid(self, token: str, user_id: str) -> bool:
        """DB에서 Refresh Token이 유효한지 검증"""
        token_entry = self.db.query(AuthUserModel).filter(
            AuthUserModel.token == token,
            AuthUserModel.user_id == user_id
        ).first()
        return token_entry is not None
