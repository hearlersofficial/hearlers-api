from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar, Optional
from uuid import UUID

from common.core.message.base_message import BaseMessage


@dataclass
class BaseCommand(BaseMessage):
    MESSAGE_TYPE: ClassVar[str] = 'baseCommand'
    command_id: UUID

    def serialize(self) -> dict:
        return {
            "command_id": self.command_id,
            "timestamp": self.timestamp.isoformat(),
            "message_type": self.MESSAGE_TYPE
        }

    @staticmethod
    def deserialize(data: dict) -> 'BaseCommand':
        return BaseCommand(
            command_id=UUID(data["command_id"]),
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
