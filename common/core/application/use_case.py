# core/application/use_case.py

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

# 제너릭 타입 정의
IRequest = TypeVar('IRequest')
IResponse = TypeVar('IResponse')

class UseCase(ABC, Generic[IRequest, IResponse]):
    @abstractmethod
    def execute(self, request: Optional[IRequest] = None) -> IResponse:
        """주어진 요청을 처리하고 응답을 반환합니다."""
        pass
