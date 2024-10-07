from datetime import datetime
from typing import ClassVar, Optional
from uuid import UUID

from common.core.infrastructure.kafka import Topic
from common.core.message.command.base_command import BaseCommand


class CreateUserCommand(BaseCommand):
    MESSAGE_TYPE: ClassVar[str] = Topic.CREATE_USER_COMMAND.value 
    def __init__(self, command_id: str, id: UUID, name: str, email: str, timestamp: Optional[datetime] = None):
        super().__init__(command_id=command_id, timestamp=timestamp)
        self.id = id
        self.name = name
        self.email = email

    def serialize(self) -> dict:
        # BaseCommand의 직렬화 로직을 확장하여 id, name, email 추가
        base_data = super().serialize()
        base_data.update({
            "id": str(self.id),
            "name": self.name,
            "email": self.email
        })
        return base_data

    @staticmethod
    def deserialize(data: dict):
        # BaseCommand의 역직렬화 로직을 사용하여 CreateUserCommand 생성
        command_id = data["command_id"]
        id = UUID(data["id"])
        name = data["name"]
        email = data["email"]
        timestamp = datetime.fromisoformat(data["timestamp"]) if "timestamp" in data else None

        return CreateUserCommand(
            command_id=command_id,
            id=id,
            name=name,
            email=email,
            timestamp=timestamp
        )
