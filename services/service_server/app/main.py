import asyncio
import logging
import os
from concurrent import futures
from contextlib import asynccontextmanager

import grpc.aio  # gRPC 비동기 서버 사용
from alembic import command, config
from dotenv import load_dotenv
from service_server.app.user import get_user_subscriber_manager

from common.core.infrastructure.subscribe_manager import SubscriberManager

# 여기에 gRPC 서비스 파일을 import해야 합니다.
# 예를 들어, UserService를 추가하려면 아래와 같이 수정
# from service_server.app.user.proto.user_pb2_grpc import add_UserServiceServicer_to_server


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()

def run_migrations():
    logger.info("Starting automatic migration")
    try:
        # DB 마이그레이션
        # command.upgrade(alembic_cfg, "head")  # 최신 마이그레이션으로 업그레이드
        logger.info("Database upgraded to the latest version")
    except Exception as e:
        logger.error(f"Error during migration: {e}")
        raise

@asynccontextmanager
async def setup_services():
    # Kafka 컨슈머 초기화
    user_subscriber_manager = await get_user_subscriber_manager()

    logger.info("Starting user subscriber manager")
    asyncio.create_task(user_subscriber_manager.start_consumers())

    # DB 마이그레이션 실행
    run_migrations()
    yield  # gRPC 서버가 종료될 때까지 서비스 유지

    # 서비스가 종료될 때 Kafka 컨슈머를 중지할 수 있습니다.
    # await user_subscriber_manager.stop_consumers()

async def serve():
    async with setup_services():
        server = grpc.aio.server()
        
        # gRPC 서비스 등록 (예: add_UserServiceServicer_to_server)
        # add_UserServiceServicer_to_server(UserService(), server)
        
        # gRPC 서버 포트 설정
        server.add_insecure_port('[::]:50051')
        logger.info("gRPC server starting on port 50051")
        
        await server.start()
        await server.wait_for_termination()

if __name__ == "__main__":
    # 비동기 gRPC 서버 실행
    asyncio.run(serve())
