# common/core/message/query/base_query.py
from datetime import datetime
from typing import ClassVar, Optional

from common.core.message.base_message import BaseMessage


class BaseQuery(BaseMessage):
    MESSAGE_TYPE: ClassVar[str] = 'baseQuery'

    def __init__(self, query_id: str, timestamp: Optional[datetime] = None):
        super().__init__(timestamp)
        self.query_id = query_id

    def serialize(self) -> dict:
        return {
            "query_id": self.query_id,
            "timestamp": self.timestamp.isoformat(),
            "message_type": self.MESSAGE_TYPE  
        }

    @staticmethod
    def deserialize(data: dict):
        return BaseQuery(
            query_id=data["query_id"],
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
