from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from uuid6 import uuid7

from common.core.domain.domain_entity import DomainEntity, DomainEntityProps
from common.core.domain.result import Result


@dataclass
class KakaoNewProps(DomainEntityProps):
    unique_id: str

@dataclass
class KakaoProps(KakaoNewProps):
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    deleted_at: Optional[datetime] = None



class Kakao(DomainEntity[KakaoProps]):
    def __init__(self, props: KakaoProps, id: UUID):
        super().__init__(props, id)

    @classmethod
    def create(cls, props: KakaoProps, id: UUID) -> Result['Kakao']:
        kakao = cls(props, id)
        return Result.ok(kakao)

    @classmethod
    def create_new(cls, props: KakaoNewProps) -> 'Result[Kakao]':
        user_props = KakaoProps(
            **props.__dict__
        )
        user_id = uuid7()  
        return cls.create(user_props, user_id)