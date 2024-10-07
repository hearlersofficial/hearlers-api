from abc import ABC, abstractmethod

from common.core.message.base_message import BaseMessage


class BaseMessageHandler(ABC):
    @abstractmethod
    def handle(self, message: BaseMessage):
        """핸들러가 처리할 메시지를 정의하는 추상 메서드"""
        pass
