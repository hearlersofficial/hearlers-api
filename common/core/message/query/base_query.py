from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar
from uuid import UUID

from common.core.message.base_message import BaseMessage


@dataclass
class BaseQuery(BaseMessage):
    MESSAGE_TYPE: ClassVar[str] = 'baseQuery'
    query_id: UUID

    def serialize(self) -> dict:
        return {
            "query_id": self.query_id,
            "timestamp": self.timestamp.isoformat(),
            "message_type": self.MESSAGE_TYPE  
        }

    @staticmethod
    def deserialize(data: dict) -> 'BaseQuery':
        return BaseQuery(
            query_id=UUID(data["query_id"]),
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
