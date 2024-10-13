
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from uuid6 import uuid7

from common.core.domain.aggregate_root import AggregateRoot, AggregateRootProps
from common.core.domain.result import Result
from common.enum.user.age_range import AgeRange
from common.enum.user.auth_channel import AuthChannel
from common.enum.user.gender import Gender


@dataclass
class UserNewProps(AggregateRootProps):
    nickname: str
    email: Optional[str]
    profile_image: Optional[str]
    phone_number: Optional[str]
    gender: Optional[Gender]
    age_range: Optional[AgeRange]
    auth_channel: AuthChannel
    kakao: Optional[str] 

# UserProps: UserNewProps를 확장하고, 자동으로 생성되는 값들을 포함
@dataclass
class UserProps(UserNewProps):
    created_at: datetime 
    updated_at: Optional[datetime] 
    deleted_at: Optional[datetime]


class User(AggregateRoot[UserProps]):
    def __init__(self, props: UserProps, id: UUID):
        super().__init__(props, id)
        self.on_create()

    @classmethod
    def createNew(cls, props: UserNewProps) -> Result['User']:
        # UserNewProps의 필드를 UserProps로 넘기고, 추가적인 필드만 설정
        user_props = UserProps(
            **props.__dict__,  # UserNewProps의 모든 필드를 가져옴
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None
        )
        # UUID 자동 생성
        user_id = uuid7()
        user = cls(user_props, user_id)
        return Result.ok(user)

    @classmethod
    def create(cls, props: UserProps, id: UUID) -> Result['User']:
        # 유저 생성 로직을 정의 (여기서는 성공적으로 생성했다고 가정)
        user = cls(props, id)
        return Result.ok(user)

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
