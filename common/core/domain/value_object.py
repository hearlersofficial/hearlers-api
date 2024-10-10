from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

T = TypeVar('T', bound='ValueObjectProps')

class ValueObjectProps:
    """ValueObject의 속성을 정의하는 기본 클래스입니다."""
    pass


class ValueObject(Generic[T], ABC):
    def __init__(self, props: T):
        self.props = props

    def equals(self, other: 'ValueObject') -> bool:
        """다른 ValueObject와 동일한지 비교합니다."""
        if not isinstance(other, ValueObject):
            return False
        return self.props == other.props

    @classmethod
    @abstractmethod
    def create(cls, props: T) -> 'ValueObject':
        """서브클래스에서 구현해야 하는 객체 생성 로직."""
        pass
