from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional


@dataclass
class BaseMessage(ABC):
    MESSAGE_TYPE: ClassVar[str] = 'baseMessage'
    timestamp: datetime

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
