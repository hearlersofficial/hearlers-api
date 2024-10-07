# common/core/message/event/base_event.py
from datetime import datetime
from typing import ClassVar, Optional
from uuid import UUID

from common.core.message.base_message import BaseMessage


class BaseEvent(BaseMessage):
    MESSAGE_TYPE: ClassVar[str] = 'baseEvent'

    def __init__(self, event_id: str, timestamp: Optional[datetime] = None):
        super().__init__(timestamp)
        self.event_id = event_id

    def serialize(self) -> dict:
        return {
            "event_id": str(self.event_id),  # UUID를 문자열로 직렬화
            "timestamp": self.timestamp.isoformat(),
            "message_type": self.MESSAGE_TYPE  # 메시지 타입을 추가하여 토픽 정보로 사용 가능
        }

    @staticmethod
    def deserialize(data: dict):
        return BaseEvent(
            event_id=data["event_id"],
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
