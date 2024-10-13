from datetime import datetime

from service_server.app.shared.infrastructure.model.user_model import UserModel
from service_server.app.user.domain.user import User, UserProps
from uuid6 import uuid7


class PsqlUserMapper:
    @staticmethod
    def to_model(user: User) -> UserModel:
        """도메인 객체를 데이터베이스 모델로 변환"""
        return UserModel(
            id=user.id,
            nickname=user.props.nickname,
            email=user.props.email,
            profile_image=user.props.profile_image,
            phone_number=user.props.phone_number,
            gender=user.props.gender,
            age_range=user.props.age_range,
            auth_channel=user.props.auth_channel,
            kakao=user.props.kakao,
            created_at=user.props.created_at,
            updated_at=user.props.updated_at,
            deleted_at=user.props.deleted_at
        )

    @staticmethod
    def to_domain(user_model: UserModel) -> User:
        """데이터베이스 모델을 도메인 객체로 변환"""
        user_props = UserProps(
            nickname=user_model.nickname,
            email=user_model.email,
            profile_image=user_model.profile_image,
            phone_number=user_model.phone_number,
            gender=user_model.gender,
            age_range=user_model.age_range,
            auth_channel=user_model.auth_channel,
            kakao=user_model.kakao,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at,
            deleted_at=user_model.deleted_at
        )
        return User(user_props, user_model.id)
    
