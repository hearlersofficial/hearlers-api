import logging
import traceback
from datetime import datetime

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

# 로깅 설정
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("ExceptionFilter")

class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response: Response = await call_next(request)
            return response
        except Exception as exc:
            return await self.handle_exception(exc, request)  # handle_exception를 비동기적으로 호출

    async def handle_exception(self, exc: Exception, request: Request) -> JSONResponse:
        http_status = 500  # 기본 내부 서버 오류 상태 코드
        message = str(exc)
        stack = traceback.format_exc()

        if isinstance(exc, HTTPException):
            http_status = exc.status_code
            message = exc.detail

        request_body = await request.body()  # 요청 본문을 비동기적으로 가져오기

        response_body = {
            "statusCode": http_status,
            "timestamp": datetime.utcnow().isoformat(),
            "path": request.url.path,
            "error": {
                "message": message,
                "stack": stack.splitlines() if stack else [],
            },
        }

        # Slack으로 전송할지 결정
        if self.need_to_send_slack(http_status):
            slack_channel = self.get_slack_channel()
            logger.error(f"Sending to Slack: Channel: {slack_channel}, Error: {message}")
            logger.error(f"Request Payload: {request_body.decode('utf-8')}")  # 바이트에서 문자열로 변환
            logger.error(stack)

        logger.error(f"{http_status} | {request.method} {request.url} | {message}")

        return JSONResponse(status_code=http_status, content=response_body)

    def need_to_send_slack(self, status_code: int) -> bool:
        return status_code == 500  # 내부 서버 오류일 경우

    def get_slack_channel(self) -> str:
        return "#channel"  # 환경에 따라 슬랙 채널 분리