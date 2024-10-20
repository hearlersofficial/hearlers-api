
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from service_server.app.user.domain.kakao import Kakao
from uuid6 import uuid7

from common.core.domain.aggregate_root import AggregateRoot, AggregateRootProps
from common.core.domain.result import Result
from common.enum.user.age_range import AgeRange
from common.enum.user.auth_channel import AuthChannel
from common.enum.user.gender import Gender


@dataclass
class UserNewProps(AggregateRootProps):
    nickname: str
    auth_channel: AuthChannel
    email: Optional[str] = None
    profile_image: Optional[str] = None
    phone_number: Optional[str] = None
    gender: Optional[Gender] = None
    age_range: Optional[AgeRange] = None
    kakao: Optional["Kakao"] = None

# UserProps: UserNewProps를 확장하고, 자동으로 생성되는 값들을 포함
@dataclass
class UserProps(UserNewProps):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    deleted_at: Optional[datetime] = None


class User(AggregateRoot[UserProps]):
    def __init__(self, props: UserProps, id: UUID):
        super().__init__(props, id)
        self.on_create()
    
    @classmethod
    def create(cls, props: UserProps, id: UUID) -> 'Result[User]':
        user = cls(props, id)
        return Result.ok(user)
    
    @classmethod
    def create_new(cls, props: UserNewProps) -> 'Result[User]':
        user_props = UserProps(
            **props.__dict__,  # UserNewProps의 모든 필드를 가져옴
        )
        user_id = uuid7()  # UUIDv7을 사용한 유저 ID 생성
        return cls.create(user_props, user_id)

    def on_create(self) -> None:
        pass
        # 유저가 생성될 때 발생하는 도메인 이벤트 추가
        # event = UserCreatedEvent(self.id)
        # self.add_domain_event(event)

    def update_email(self, new_email: str) -> None:
        """유저의 이메일을 업데이트하는 메서드."""
        self.props.email = new_email

    def update_profile(self, **kwargs) -> None:
        """유저의 프로필 정보를 업데이트하는 메서드."""
        for key, value in kwargs.items():
            if hasattr(self.props, key) and value is not None:
                setattr(self.props, key, value)
