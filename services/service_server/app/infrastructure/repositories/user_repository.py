from abc import ABC, abstractmethod
from uuid import UUID

from service_server.app.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User:
        pass
