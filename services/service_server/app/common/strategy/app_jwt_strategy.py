import os
from typing import Optional

from jose import JWTError, jwt

from common.core.infrastructure.configs import Settings
from common.strategy.jwt_strategy import JWTStrategy


class AppJWTStrategy(JWTStrategy):
    def __init__(self):
        self.secret_key = Settings.APP_JWT_SECRET
        self.refresh_secret_key = Settings.APP_JWT_SECRET
        self.algorithm = "HS256"

    def validate_access_token(self, token: str) -> Optional[dict]:
        """JWT Access Token을 검증하고, 유효하면 페이로드를 반환"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            return None

    def validate_refresh_token(self, token: str) -> Optional[dict]:
        """JWT Refresh Token을 검증하고, 유효하면 페이로드를 반환"""
        try:
            payload = jwt.decode(token, self.refresh_secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            return None
