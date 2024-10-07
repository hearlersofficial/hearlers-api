# common/models/aggregate_root.py
from abc import ABC, abstractmethod
from typing import Any, Generic, List, TypeVar
from uuid import UUID

from common.core.domain.result import Result
from common.core.event.base_event import BaseEvent


class AggregateRootProps:
    """AggregateRoot의 속성을 정의하는 기본 클래스입니다."""
    pass


T = TypeVar('T', bound='AggregateRootProps')

class AggregateRoot(Generic[T], ABC):
    def __init__(self, props: T, id: UUID):
        self._id = id
        self._domain_events: List[BaseEvent] = []
        self.props = props

    @abstractmethod
    def on_create(self) -> None:
        """서브클래스에서 구현해야 하는 생성 로직."""
        pass

    @classmethod
    @abstractmethod
    def create(cls, props: T, id: UUID) -> Result['AggregateRoot[T]']:
        """서브클래스에서 구현해야 하는 객체 생성 로직."""
        pass

    def equals(self, other: 'AggregateRoot') -> bool:
        """다른 AggregateRoot와 동일한지 비교합니다."""
        return isinstance(other, AggregateRoot) and self.id == other.id    

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def domain_events(self) -> List[Any]:
        return self._domain_events

    def add_domain_event(self, event: BaseEvent) -> None:
        """도메인 이벤트를 추가합니다."""
        self._domain_events.append(event)

    def clear_domain_events(self) -> None:
        """도메인 이벤트를 초기화합니다."""
        self._domain_events = []
