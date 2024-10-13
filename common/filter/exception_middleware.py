import logging
import traceback
from datetime import datetime

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

# 로깅 설정
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("ExceptionFilter")

async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    http_status = 500  # 기본 상태 코드
    message = str(exc)
    stack = traceback.format_exc()

    # HTTPException일 경우 상태 코드 및 메시지 변경
    if isinstance(exc, HTTPException):
        http_status = exc.status_code
        message = exc.detail

    request_body = await request.body()  # 요청 본문 가져오기

    response_body = {
        "statusCode": http_status,
        "timestamp": datetime.utcnow().isoformat(),
        "path": request.url.path,
        "error": {
            "message": message,
            "stack": stack.splitlines() if stack else [],
        },
    }

    # 500 에러인 경우 Slack으로 전송 (예시)
    if http_status == 500:
        slack_channel = "#channel"
        logger.error(f"Sending to Slack: Channel: {slack_channel}, Error: {message}")
        logger.error(f"Request Payload: {request_body.decode('utf-8')}")
        logger.error(stack)

    # 로그 기록
    logger.error(f"{http_status} | {request.method} {request.url} | {message}")

    return JSONResponse(status_code=http_status, content=response_body)
