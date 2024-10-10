import os
from pathlib import Path

from dotenv import load_dotenv

# .env 파일 로드
env_path = Path(__file__).parent / "../../../" / os.getenv('ENV_FILE', '.env.dev')
load_dotenv(dotenv_path=env_path)

def get_env_variable(var_name: str) -> str:
    """환경 변수를 가져오고, 없을 경우 오류를 발생시킵니다."""
    value = os.getenv(var_name)
    if value is None:
        raise EnvironmentError(f"환경 변수 {var_name}이(가) 설정되지 않았습니다.")
    return value

class Settings:
    # FastAPI 및 기타 설정
    DEBUG = get_env_variable('DEBUG').lower() == 'true'
    APP_HOST = get_env_variable('APP_HOST')
    APP_PORT = int(get_env_variable('APP_PORT'))

    # PostgreSQL 설정
    DATABASE_USER = get_env_variable('DATABASE_USER')
    DATABASE_PASSWORD = get_env_variable('DATABASE_PASSWORD')
    DATABASE_HOST = get_env_variable('DATABASE_HOST')
    DATABASE_PORT = int(get_env_variable('DATABASE_PORT'))
    DATABASE_NAME = get_env_variable('DATABASE_NAME')

    # SQLAlchemy 설정 (옵션)
    SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    ECHO_SQL = get_env_variable('ECHO_SQL').lower() == 'true'

    # Kafka 설정
    KAFKA_BOOTSTRAP_SERVERS = get_env_variable('KAFKA_BOOTSTRAP_SERVERS')

    #JWT 설정
    APP_JWT_SECRET = get_env_variable('APP_JWT_SECRET')
# 설정 객체 생성 및 확인
try:
    settings = Settings()
except EnvironmentError as e:
    print(e)
