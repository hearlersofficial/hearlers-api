# common/core/message/command/base_command.py
from datetime import datetime
from typing import ClassVar, Optional
from uuid import UUID

from common.core.message.base_message import BaseMessage


class BaseCommand(BaseMessage):
    MESSAGE_TYPE: ClassVar[str] = 'baseCommand'

    def __init__(self, command_id: str, timestamp: Optional[datetime] = None):
        super().__init__(timestamp)
        self.command_id = command_id

    def serialize(self) -> dict:
        return {
            "command_id": str(self.command_id),  # UUID를 문자열로 직렬화
            "timestamp": self.timestamp.isoformat(),
            "message_type": self.MESSAGE_TYPE  # 메시지 타입을 추가하여 토픽 정보로 사용 가능
        }

    @staticmethod
    def deserialize(data: dict):
        return BaseCommand(
            command_id=data["command_id"],
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
