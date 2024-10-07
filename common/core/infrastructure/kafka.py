# common/kafka_utils.py
import json
from enum import Enum
from typing import Any, Type

from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError  # 올바른 import 경로

from common.core.application.message_bus import MessageBus
from common.core.message.base_message import BaseMessage


class Topic(Enum):
    # Commands
    CREATE_USER_COMMAND = "create.user.command"
    UPDATE_USER_COMMAND = "update.user.command"
    DELETE_USER_COMMAND = "delete.user.command"
    
    CREATE_ORDER_COMMAND = "create.order.command"
    CANCEL_ORDER_COMMAND = "cancel.order.command"
    
    # Queries
    GET_USER_QUERY = "get.user.query"
    LIST_USERS_QUERY = "list.users.query"
    
    GET_ORDER_QUERY = "get.order.query"
    LIST_ORDERS_QUERY = "list.orders.query"
    
    # Events
    USER_CREATED = "user.created"
    USER_UPDATED = "user.updated"
    USER_DELETED = "user.deleted"
    
    ORDER_CREATED = "order.created"
    ORDER_CANCELED = "order.canceled"

    @classmethod
    def list_topics(cls):
        """모든 토픽 리스트 반환"""
        return [topic.value for topic in cls]

class MessageProducer:
    def __init__(self, bootstrap_servers: str):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_message(self, message: BaseMessage) -> None:
        """메시지를 지정된 Kafka 토픽에 전송합니다."""
        self.producer.send(message.MESSAGE_TYPE, message.serialize())
        self.producer.flush()


class MessageConsumer:
    def __init__(self, topic: Topic, bootstrap_servers: str, group_id: str, message_bus: MessageBus):
        self.consumer = KafkaConsumer(
            topic.value,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        self.message_bus = message_bus
        self._is_running = False

    def consume_messages(self) -> None:
        """메시지를 소비하고 처리하는 메서드입니다."""
        self._is_running = True
        try:
            for message in self.consumer:
                if not self._is_running:
                    break
                message_data = message.value
                message_type = message_data.get("message_type")
                if not message_type:
                    print("Received message without type field.")
                    continue

                # Message 객체 생성 및 디스패치
                msg = self.message_bus.create_message(message_data)
                if msg:
                    self.message_bus.dispatch(msg)
                else:
                    print(f"Unknown message type: {message_type}")
        except KafkaError as e:
            print(f"Kafka error: {e}")
        finally:
            self.consumer.close()
            print(f"Consumer for topic {self.consumer.subscription()} closed.")

    def stop(self):
        """소비자 중지를 요청합니다."""
        self._is_running = False
        self.consumer.close()
