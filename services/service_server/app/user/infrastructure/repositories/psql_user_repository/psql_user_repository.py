from typing import List, Optional
from uuid import UUID

from fastapi import Depends
from service_server.app.shared.infrastructure.db import get_db_session
from service_server.app.shared.infrastructure.model.user_model import UserModel
from service_server.app.user.domain.user import User
from service_server.app.user.infrastructure.repositories.psql_user_repository.mapper.psql_user_mapper import \
    PsqlUserMapper
from service_server.app.user.infrastructure.repositories.user_repository import (
    FindManyPropsInUserRepository, FindOnePropsInUserRepository,
    UserRepository)
from sqlalchemy.orm import Session

from common.enum.user.auth_channel import AuthChannel


class PSQLUserRepository(UserRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, user: User) -> User:
        """도메인 객체를 데이터베이스 모델로 변환한 후 저장"""
        user_model = PsqlUserMapper.to_model(user)
        self.db_session.add(user_model)
        self.db_session.commit()
        return PsqlUserMapper.to_domain(user_model) 

    def find_one(self, props: FindOnePropsInUserRepository) -> Optional[User]:
        """주어진 user_id로 단일 사용자 조회"""
        user_model = self.db_session.query(UserModel).filter(UserModel.id == props.user_id).first()
        if user_model:
            return PsqlUserMapper.to_domain(user_model)
        return None

    def find_many(self, props: FindManyPropsInUserRepository) -> List[User]:
        """주어진 auth_channel로 여러 사용자 조회"""
        user_models = self.db_session.query(UserModel).filter(UserModel.auth_channel == props.auth_channel).all()
        return [PsqlUserMapper.to_domain(user_model) for user_model in user_models]

def get_user_repository(db_session: Session = Depends(get_db_session)) -> UserRepository:
    return PSQLUserRepository(db_session)