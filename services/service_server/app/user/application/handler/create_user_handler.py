from venv import logger

from service_server.app.user.domain.user import User, UserProps
from service_server.app.user.infrastructure.repositories.psql_user_repository.psql_user_repository import \
    PsqlUserRepository

from common.core.application.base_message_handler import BaseMessageHandler
from common.core.dependency.dependency_injection import get_message_bus
from common.core.message.command.user.user_command import CreateUserCommand


class CreateUserHandler(BaseMessageHandler):
    def __init__(self, repository=None):
        self.repository = repository or PsqlUserRepository()
        logger.info("CreateUserHandler initialized")


    def handle(self, message: CreateUserCommand):
        user = User(props=UserProps(username=message.name,email=message.email), id = message.id)
        logger.info(f"User created: {user}")

