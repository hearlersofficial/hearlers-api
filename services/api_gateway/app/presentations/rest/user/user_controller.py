# services/api_gateway/app/api/user.py
import json
import os
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from common.core.dependency.dependency_injection import get_message_producer
from common.core.infrastructure.kafka import MessageProducer
from common.core.message.command.user.user_command import CreateUserCommand

router = APIRouter()

class CreateUserRequest(BaseModel):
    id: UUID
    name: str
    email: str

@router.post("/", response_model=dict)
def create_user(request: CreateUserRequest, producer: MessageProducer = Depends(get_message_producer)):
    try:
        message = CreateUserCommand(id=request.id, command_id= str(uuid4()),name=request.name, email=request.email)
        producer.send_message(message)
        return {"success": True, "message": "User creation event sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))