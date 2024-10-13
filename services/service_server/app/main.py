import asyncio
import logging
import os
from contextlib import asynccontextmanager

from alembic import command, config
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from service_server.app.user import get_user_subscriber_manager
from service_server.app.user.controller.user_controller import user_router

from common.core.infrastructure.subscribe_manager import SubscriberManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()
# alembic_cfg = config.Config(os.path.join(os.path.dirname(__file__), 'alembic.ini'))
# script_location = os.path.join(os.path.dirname(__file__), 'alembic')
# alembic_cfg.set_main_option("script_location", script_location)

def run_migrations():
    logger.info("Starting automatic migration")
    try:
        # 직접 비동기 작업 호출
        # command.revision(alembic_cfg, message="automatic migration", autogenerate=True)
        # logger.info("Migration files created successfully")

        # command.upgrade(alembic_cfg, "head")  # 최신 마이그레이션으로 업그레이드
        logger.info("Database upgraded to the latest version")
    except Exception as e:
        logger.error(f"Error during migration: {e}")
        raise


@asynccontextmanager
async def lifespan(app: FastAPI):

    user_subscriber_manager = await get_user_subscriber_manager()

    logger.info("Starting user subscriber manager")
    # 컨슈머 시작
    asyncio.create_task(user_subscriber_manager.start_consumers())
    
    run_migrations()
    yield
    
    # 컨슈머 중지
    # await user_subscriber_manager.stop_consumers()

app = FastAPI(lifespan=lifespan)


app.include_router(user_router, prefix="/users")
# app.include_router(chat_router, prefix="/chats")


@app.get("/")
def read_root():
    return {"message": "User Service is running"}