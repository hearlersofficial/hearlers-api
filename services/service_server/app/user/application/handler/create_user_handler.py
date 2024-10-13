from venv import logger

from service_server.app.user.domain.user import User, UserProps

from common.core.application.base_message_handler import BaseMessageHandler
from common.core.dependency.dependency_injection import get_message_bus
from common.core.message.command.user.auth.create_kakao_user_command import \
    CreateKakaoUserCommand


class CreateKakaoUserHandler(BaseMessageHandler):
    def __init__(self, repository=None):
        # self.repository = repository or PsqlUserRepository()
        logger.info("CreateUserHandler initialized")


    def handle(self, message: CreateKakaoUserCommand):
        return;

