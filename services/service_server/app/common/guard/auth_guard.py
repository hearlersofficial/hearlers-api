from typing import Optional

from fastapi import HTTPException, Request, status

from common.service.jwt_service import JWTService
from common.strategy.app_jwt_strategy import JWTStrategy


class AuthGuard:
    def __init__(self, strategy: JWTStrategy, jwt_service: JWTService):
        self.strategy = strategy
        self.jwt_service = jwt_service

    async def get_current_user(self, request: Request) -> Optional[dict]:
        """Access Token을 검증하고 유저 정보를 반환"""
        authorization_header = request.headers.get("Authorization")
        if not authorization_header or not authorization_header.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authorization header missing or invalid",
            )
        
        token = authorization_header.split(" ")[1]
        user_info = self.jwt_service.get_user_from_access_token(token, self.strategy)
        if not user_info:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
        
        return user_info

    async def validate_refresh_token(self, refresh_token: str, user_id: str) -> bool:
        """Refresh Token 검증"""
        is_valid = self.jwt_service.is_refresh_token_valid(refresh_token, user_id)
        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
            )
        return is_valid
