from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

from common.core.infrastructure.kafka import Topic
from common.core.message.command.base_command import BaseCommand


@dataclass
class CreateKakaoUserCommand(BaseCommand):
    MESSAGE_TYPE: ClassVar[str] = Topic.CREATE_KAKAO_USER_COMMAND.value
    code: str
    state: str

    def serialize(self) -> dict:
        base_data = super().serialize()
        base_data.update({"code": self.code, "state": self.state})
        return base_data

    @staticmethod
    def deserialize(data: dict) -> 'CreateKakaoUserCommand':
        return CreateKakaoUserCommand(
            command_id=data["command_id"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            code=data["code"],
            state=data["state"]
        )
