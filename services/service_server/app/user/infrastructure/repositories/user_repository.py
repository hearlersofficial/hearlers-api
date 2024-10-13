from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID

from service_server.app.user.domain.user import User

from common.enum.user.auth_channel import AuthChannel


@dataclass
class FindOnePropsInUserRepository:
    user_id: UUID

@dataclass
class FindManyPropsInUserRepository:
    auth_channel: AuthChannel

class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def find_one(self, props: FindOnePropsInUserRepository) -> Optional[User]:
        pass

    @abstractmethod
    def find_many(self, props: FindManyPropsInUserRepository) -> List[User]:
        pass
