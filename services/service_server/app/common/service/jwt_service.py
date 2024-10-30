from abc import ABC, abstractmethod
from typing import Optional


class JWTService(ABC):
    @abstractmethod
    def is_refresh_token_valid(self, token: str, user_id: str) -> bool:
        """DB에서 Refresh Token이 유효한지 검증하는 메서드"""
        pass

    def get_user_from_access_token(self, token: str, strategy) -> Optional[dict]:
        """Access Token으로 유저 정보를 가져오는 공통 메서드"""
        payload = strategy.validate_access_token(token)
        if payload:
            return {"user_id": payload.get("sub")}
        return None

    def get_user_from_refresh_token(self, token: str, strategy) -> Optional[dict]:
        """Refresh Token으로 유저 정보를 가져오는 공통 메서드"""
        payload = strategy.validate_refresh_token(token)
        if payload:
            return {"user_id": payload.get("sub")}
        return None
