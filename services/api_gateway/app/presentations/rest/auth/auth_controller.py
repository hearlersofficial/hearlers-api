# services/api_gateway/app/api/user.py
import json
import os
from datetime import datetime
from uuid import UUID, uuid4

from api_gateway.app.presentations.rest.auth.dto.login.login_request import \
    LoginRequest
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from uuid6 import uuid7

from common.core.dependency.dependency_injection import get_message_producer
from common.core.infrastructure.kafka import MessageProducer
from common.core.message.base_message import BaseMessage
from common.core.message.command.user.auth.create_kakao_user_command import \
    CreateKakaoUserCommand
from common.enum.user.auth_channel import AuthChannel

auth_router = APIRouter()


@auth_router.post("/login", response_model=dict)
def create_user(request: LoginRequest, producer: MessageProducer = Depends(get_message_producer)):
    try:
        message: BaseMessage
        if(request.authChannel == AuthChannel.KAKAO):
            message = CreateKakaoUserCommand(command_id= uuid7(),code=request.code, state=request.state, timestamp=datetime.now())
        producer.send_message(message)
        return {"success": True, "message": "User creation event sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))