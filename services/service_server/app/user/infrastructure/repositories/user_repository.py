from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from service_server.app.user.domain.user import User


class FindOnePropsInUserRepository:
    def __init__(self, user_id: Optional[UUID] = None, email: Optional[str] = None):
        self.user_id = user_id
        self.email = email

class FindManyPropsInUserRepository:
    def __init__(self, user_id: Optional[UUID] = None, email: Optional[str] = None):
        self.user_id = user_id
        self.email = email

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass

    @abstractmethod
    def find_one(self, props: FindOnePropsInUserRepository) -> Optional[User]:
        pass

    @abstractmethod
    def find_many(self, props: FindManyPropsInUserRepository) -> List[User]:
        pass
