# app/user/application/router.py
from fastapi import APIRouter
from service_server.app.user.application.handler.create_user_handler import \
    CreateUserHandler

from common.core.dependency.dependency_injection import get_message_bus
from common.core.infrastructure.configs import Settings
from common.core.infrastructure.kafka import Topic
from common.core.infrastructure.subscribe_manager import SubscriberManager
from common.core.message.command.user.user_command import CreateUserCommand


async def get_user_subscriber_manager():
    message_bus = get_message_bus()
    
    subscriber_manager = SubscriberManager(
        message_bus=message_bus,
        bootstrap_servers=Settings.KAFKA_BOOTSTRAP_SERVERS
    )
    
    # 유저 도메인 관련 컨슈머 등록
    subscriber_manager.register_consumer(
        topic=Topic.CREATE_USER_COMMAND, 
        message_class=CreateUserCommand, 
        handler_class=CreateUserHandler, 
        group_id="user-service-group"
    )
    
    return subscriber_manager


