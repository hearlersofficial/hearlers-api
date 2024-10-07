# common/subscriber_manager.py
import asyncio
from typing import List, Type

from common.core.application.base_message_handler import BaseMessageHandler
from common.core.application.message_bus import MessageBus
from common.core.infrastructure.kafka import MessageConsumer, Topic
from common.core.message.base_message import BaseMessage


class SubscriberManager:
    def __init__(self, message_bus: MessageBus, bootstrap_servers: str):
        self.message_bus = message_bus
        self.bootstrap_servers = bootstrap_servers
        self.consumers: List[MessageConsumer] = []
        self.tasks: List[asyncio.Task] = []

    def register_consumer(
        self,
        topic: Topic,
        group_id: str,
        message_class: Type[BaseMessage],
        handler_class: Type[BaseMessageHandler]
    ):
        # 메시지 클래스 등록
        self.message_bus.register_message(message_class)
        # 핸들러 클래스 등록
        self.message_bus.register_handler(message_class, handler_class)

        consumer = MessageConsumer(
            topic=topic,
            bootstrap_servers=self.bootstrap_servers,
            group_id=group_id,
            message_bus=self.message_bus
        )
        self.consumers.append(consumer)

    async def start_consumers(self):
        for consumer in self.consumers:
            # asyncio.to_thread을 사용하여 동기 함수를 비동기적으로 실행
            task = asyncio.create_task(asyncio.to_thread(consumer.consume_messages))
            self.tasks.append(task)
        # 모든 태스크를 동시 실행
        await asyncio.gather(*self.tasks)

    async def stop_consumers(self):
        # 모든 소비자에게 중지 신호를 보냄
        for consumer in self.consumers:
            consumer.stop()
        # 소비자 스레드가 종료될 때까지 대기
        await asyncio.gather(*self.tasks, return_exceptions=True)
