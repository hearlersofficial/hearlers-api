from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar
from uuid import UUID

from common.core.message.base_message import BaseMessage


@dataclass
class BaseEvent(BaseMessage):
    MESSAGE_TYPE: ClassVar[str] = 'baseEvent'
    event_id: UUID

    def serialize(self) -> dict:
        return {
            "event_id": str(self.event_id),  # UUID를 문자열로 직렬화
            "timestamp": self.timestamp.isoformat(),
            "message_type": self.MESSAGE_TYPE
        }

    @staticmethod
    def deserialize(data: dict) -> 'BaseEvent':
        return BaseEvent(
            event_id=UUID(data["event_id"]),
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
