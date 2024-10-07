# services/api_gateway/app/api/user.py
import json
import os
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from common.utils.kafka import get_kafka_producer

router = APIRouter()

class CreateUserRequest(BaseModel):
    id: UUID
    name: str
    email: str

@router.post("/", response_model=dict)
def create_user(request: CreateUserRequest, producer = Depends(get_kafka_producer)):
    try:
        message = request.model_dump()
        producer.send('create_user_topic', value=message)
        producer.flush()
        return {"success": True, "message": "User creation event sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
