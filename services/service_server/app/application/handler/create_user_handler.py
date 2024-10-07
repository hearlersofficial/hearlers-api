from venv import logger

from service_server.app.domain.user import User
from service_server.app.infrastructure.repositories.psql_user_repository.psql_user_repository import \
    PsqlUserRepository

from common.core.application.base_message_handler import BaseMessageHandler
from common.core.dependency.dependency_injection import get_message_bus
from common.core.message.command.user.user_command import CreateUserCommand


class CreateUserHandler(BaseMessageHandler):
    def __init__(self, repository=None):
        self.repository = repository or PsqlUserRepository()
        logger.info("CreateUserHandler initialized")


    def handle(self, message: CreateUserCommand):
        user = User(id=message.id, name=message.name, email=message.email)
        logger.info(f"User created: {user}")

