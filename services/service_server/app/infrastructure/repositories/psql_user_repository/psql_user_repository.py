from uuid import UUID

from service_server.app.infrastructure.db import SessionLocal
from service_server.app.infrastructure.models.user import UserModel
from service_server.app.infrastructure.repositories.user_repository import \
    UserRepository


class PsqlUserRepository(UserRepository):
    def __init__(self):
        self.session = SessionLocal()

    def save(self, user: UserModel):
        user_entity = UserModel(
            id=user.id,
            name=user.name,
            email=user.email
        )
        self.session.add(user_entity)
        self.session.commit()

    def get_by_id(self, user_id: UUID) -> UserModel:
        user_entity = self.session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_entity:
            return UserModel(id=user_entity.id, name=user_entity.name, email=user_entity.email)
        return UserModel
