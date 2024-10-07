#!/bin/bash

# 종료 처리 함수
function shutdown() {
    echo "서버 종료 중..."
    kill -TERM $api_gateway_pid $user_service_pid
    wait
    echo "모든 서버가 종료되었습니다."
}

# SIGINT 및 SIGTERM 신호를 처리하여 서버 종료
trap shutdown SIGINT SIGTERM

# 서버 실행 메시지
echo "모든 MSA 서버를 시작합니다..."

# .env 파일을 읽어 환경 변수로 설정
set -o allexport
source .env.local
set +o allexport

# API Gateway 서버 실행 및 PID 저장
poetry run env PYTHONPATH=$(pwd)/services uvicorn services.api_gateway.app.main:app --host 0.0.0.0 --port 8000 --reload &
api_gateway_pid=$!
echo "API Gateway 서버 실행 중 (포트 8000, PID: $api_gateway_pid)"

# User Service 서버 실행 및 PID 저장
poetry run env PYTHONPATH=$(pwd)/services uvicorn services.service_server.app.main:app --host 0.0.0.0 --port 8001 --reload &
user_service_pid=$!
echo "User Service 서버 실행 중 (포트 8001, PID: $user_service_pid)"

# 모든 백그라운드 프로세스가 종료될 때까지 대기
wait
