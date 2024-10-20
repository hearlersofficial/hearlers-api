from venv import logger

from fastapi import Depends
from service_server.app.user.domain.kakao import Kakao, KakaoProps
from service_server.app.user.domain.user import User, UserNewProps, UserProps
from service_server.app.user.infrastructure.repositories.psql_user_repository.psql_user_repository import \
    get_user_repository
from service_server.app.user.infrastructure.repositories.user_repository import \
    UserRepository
from uuid6 import uuid7

from common.core.application.base_message_handler import BaseMessageHandler
from common.core.domain.result import Result
from common.core.message.command.user.auth.create_kakao_user_command import \
    CreateKakaoUserCommand
from common.enum.user.auth_channel import AuthChannel


class CreateKakaoUserHandler(BaseMessageHandler):
    def __init__(self):
        logger.info("CreateUserHandler initialized")


    def handle(self, message:CreateKakaoUserCommand):
        # 메시지 처리 시점에 의존성 주입 (예: DB 세션)
        repository = get_user_repository()
        # Todo: 카카오 api 연동하기
        kakao_or_error: Result[Kakao] = Kakao.create_new(KakaoProps(unique_id=str(uuid7())))
        if kakao_or_error.is_failure:
            raise Exception(f"카카오 생성 실패: {kakao_or_error.error}")
    
        kakao = kakao_or_error.value

        user_or_error = User.create_new(UserNewProps(nickname=str(uuid7()), auth_channel=AuthChannel.KAKAO, kakao=kakao))
        if user_or_error.is_failure:
            raise Exception(f"유저 생성 실패: {user_or_error.error}")
        user = user_or_error.value
        saved_user = repository.create(user)
        logger.info(f"유저 생성함, {saved_user}, with code={message.code}, state={message.state}")
        return;

