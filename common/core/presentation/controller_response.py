# core/application/controller_error.py

from typing import List, Optional

from pydantic import BaseModel, Field


class ControllerError(BaseModel):
    message: str = Field(..., description="에러에 대한 대략적 설명")
    stack: Optional[List[str]] = Field(None, description="error stack")


class ControllerResponse(BaseModel):
    statusCode: int = Field(..., description="HTTP status code")
    ok: bool = Field(..., description="Response success")


class ControllerInternalErrorResponse(BaseModel):
    statusCode: int = Field(..., description="HTTP status code")
    ok: bool = Field(..., description="Response success")
    error: ControllerError = Field(..., description="에러 정보")
