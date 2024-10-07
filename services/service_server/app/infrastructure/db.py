# services/user_service/app/infrastructure/db.py
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
BASE_DIR = Path(__file__).resolve().parent.parent.parent

if not all([os.getenv('DATABASE_USER'), os.getenv('DATABASE_PASSWORD'), os.getenv('DATABASE_HOST'), os.getenv('DATABASE_PORT'), os.getenv('DATABASE_NAME')]):
    raise EnvironmentError(f"필수 DATABASE 환경 변수가 누락되었습니다. {DATABASE_URL}, ")




engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
