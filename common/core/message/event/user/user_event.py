# common/events/user_events.py
from datetime import datetime
from typing import ClassVar, Optional
from uuid import UUID

from common.core.message.event.base_event import BaseEvent


class UserCreatedEvent(BaseEvent):
    MESSAGE_TYPE: ClassVar[str] = "UserCreatedEvent"  
    user_id: UUID
    name: str
    email: str

    def __init__(self, event_id: str, user_id: UUID, username: str, email: str, timestamp: Optional[datetime] = None):
        super().__init__(event_id=event_id,timestamp=timestamp)
        self.user_id = user_id
        self.username = username
        self.email = email

    def serialize(self) -> dict:
        return {
            "message_type": self.MESSAGE_TYPE,
            "timestamp": self.timestamp.isoformat(),
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email
        }

    @staticmethod
    def deserialize(data: dict):
        return UserCreatedEvent(
            event_id=data["event_id"],
            user_id=data["user_id"],
            username=data["username"],
            email=data["email"]
        )