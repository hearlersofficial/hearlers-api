# common/core/message/base_message.py
from abc import ABC, abstractmethod
from datetime import datetime
from typing import ClassVar, Optional


class BaseMessage(ABC):
    MESSAGE_TYPE: ClassVar[str] = 'baseMessage'

    def __init__(self, timestamp: Optional[datetime] = None):
        self._timestamp = timestamp if timestamp is not None else datetime.now()

    @abstractmethod
    def serialize(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def deserialize(data: dict):
        pass

    @property
    def message_type(self) -> str:
        return self.__class__.MESSAGE_TYPE

    @property
    def timestamp(self) -> datetime:
        return self._timestamp
