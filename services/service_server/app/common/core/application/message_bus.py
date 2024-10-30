# common/message_bus.py
import logging
from typing import Dict, Optional, Type, TypeVar

from common.core.application.base_message_handler import BaseMessageHandler
from common.core.message.base_message import BaseMessage

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

T = TypeVar('T', bound=BaseMessage)

class MessageBus:
    def __init__(self):
        self._handlers: Dict[str, BaseMessageHandler] = {}
        self._message_classes: Dict[str, Type[BaseMessage]] = {}
        logger.info("MessageBus initialized.")

    def register_message(self, message_class: Type[BaseMessage]):
        """메시지 클래스를 그 타입과 함께 등록합니다."""
        message_type = message_class.MESSAGE_TYPE
        if not isinstance(message_type, str):
            raise TypeError("MESSAGE_TYPE must be a string")
        self._message_classes[message_type] = message_class
        logger.info(f"Message class registered: {message_type} with class {message_class.__name__}")

    def register_handler(self, message_class: Type[BaseMessage], handler_class: Type[BaseMessageHandler]):
        """명시적으로 메시지 타입에 대한 핸들러를 등록합니다."""
        message_type = message_class.MESSAGE_TYPE
        if not isinstance(message_type, str):
            raise TypeError("message_type must be a string")
        logger.info(f"Registering handler for message type: {message_type} with handler class: {handler_class.__name__}")
        try:
            handler_instance = handler_class()
            self._handlers[message_type] = handler_instance
            logger.info(f"Handler instance created for message type: {message_type} with handler: {handler_instance.__class__.__name__}")
        except Exception as e:
            logger.error(f"Failed to create handler instance for message type: {message_type}. Error: {e}")
            raise

    def dispatch(self, message: BaseMessage):
        """메시지 타입에 따라 등록된 핸들러에 메시지를 디스패치합니다."""
        message_type = message.message_type
        logger.info(f"Dispatching message of type: {message_type}")
        handler = self._handlers.get(message_type)
        if handler:
            logger.info(f"Found handler for message type: {message_type}. Handler: {handler.__class__.__name__}")
            try:
                handler.handle(message)  # 핸들러의 handle 메서드 호출
                logger.info(f"Message of type: {message_type} handled successfully by {handler.__class__.__name__}")
            except Exception as e:
                logger.error(f"Error while handling message of type: {message_type} with handler {handler.__class__.__name__}. Error: {e}")
                raise
        else:
            logger.warning(f"No handler registered for message type: {message_type}")

    def create_message(self, message_data: dict) -> Optional[BaseMessage]:
        """메시지 타입에 기반하여 메시지 객체를 인스턴스화합니다."""
        message_type = message_data.get("message_type")
        if not isinstance(message_type, str):
            logger.error("message_type is missing or not a string in message data.")
            return None
        message_class = self._message_classes.get(message_type)
        if message_class:
            logger.info(f"Creating message instance of type: {message_type} with class {message_class.__name__}")
            try:
                message_instance = message_class.deserialize(message_data)
                logger.info(f"Message instance created for type: {message_type}")
                return message_instance
            except Exception as e:
                logger.error(f"Failed to deserialize message of type: {message_type}. Error: {e}")
                return None
        else:
            logger.error(f"Unknown message type: {message_type}")
            return None
