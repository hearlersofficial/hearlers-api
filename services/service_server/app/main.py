import asyncio
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from service_server.app.application.handler.create_user_handler import \
    CreateUserHandler
from service_server.app.infrastructure.db import init_db

from common.core.dependency.dependency_injection import get_message_bus
from common.core.infrastructure.configs import Settings
from common.core.infrastructure.kafka import Topic
from common.core.infrastructure.subscribe_manager import SubscriberManager
from common.core.message.command.user.user_command import CreateUserCommand

# .env 파일 로드
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    message_bus=get_message_bus();

    subscriber_manager = SubscriberManager(
        message_bus=message_bus,
        bootstrap_servers=Settings.KAFKA_BOOTSTRAP_SERVERS
    )
    
    # 컨슈머 등록
    subscriber_manager.register_consumer(topic=Topic.CREATE_USER_COMMAND, message_class=CreateUserCommand,handler_class=CreateUserHandler,group_id="service-server-group")
    
    # 컨슈머 시작
    asyncio.create_task(subscriber_manager.start_consumers())
    print("애플리케이션 시작: 컨슈머 시작됨.")
    
    # 핸들러 등록
    message_bus.register_handler(CreateUserCommand,CreateUserHandler)
    yield
    
    # 컨슈머 중지
    await subscriber_manager.stop_consumers()
    print("애플리케이션 종료: 컨슈머 중지됨.")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "User Service is running"}