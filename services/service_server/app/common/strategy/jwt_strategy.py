from abc import ABC, abstractmethod
from typing import Optional


class JWTStrategy(ABC):
    @abstractmethod
    def validate_access_token(self, token: str) -> Optional[dict]:
        """JWT Access Token을 검증하고 유효한 페이로드 반환"""
        pass

    @abstractmethod
    def validate_refresh_token(self, token: str) -> Optional[dict]:
        """JWT Refresh Token을 검증하고 유효한 페이로드 반환"""
        pass
