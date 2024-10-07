# common/core/dependencies.py
from fastapi import Depends

from common.core.application.message_bus import MessageBus
from common.core.infrastructure.configs import Settings
from common.core.infrastructure.kafka import MessageProducer

# 모듈 레벨에서 단일 인스턴스 생성
bootstrap_servers = Settings.KAFKA_BOOTSTRAP_SERVERS
message_producer_instance = MessageProducer(bootstrap_servers=bootstrap_servers)
message_bus_instance = MessageBus()

def get_message_producer() -> MessageProducer:
    return message_producer_instance

def get_message_bus() -> MessageBus:
    return message_bus_instance
