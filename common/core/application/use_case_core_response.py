from dataclasses import dataclass, field
from typing import Optional


@dataclass
class UseCaseCoreResponse:
    ok: bool = field(default=False)  # 기본값으로 False 설정
    error: Optional[str] = field(default=None)  # 오류 메시지 기본값 설정