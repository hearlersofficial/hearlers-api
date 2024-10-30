# common/result.py

from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class Result(Generic[T]):
    def __init__(self, is_success: bool, error: Optional[str] = None, value: Optional[T] = None):
        self._value: Optional[T] = value
        self.error: Optional[str] = error
        self.is_success: bool = is_success
        self.is_failure: bool = not is_success

        # 불변 객체로 만들기
        self._freeze()

    def _freeze(self):
        """객체를 불변으로 만듭니다."""
        object.__setattr__(self, "_frozen", True)

    @property
    def value(self) -> T:
        if not self.is_success:
            raise Exception(self.error)
        return self._value  # type: ignore

    @property
    def error_value(self) -> Optional[str]:
        return self.error

    @classmethod
    def ok(cls, value: Optional[T] = None) -> 'Result[T]':
        """성공적인 결과를 생성합니다."""
        return cls(True, None, value)

    @classmethod
    def fail(cls, error: str) -> 'Result[T]':
        """실패한 결과를 생성합니다."""
        return cls(False, error)

    @classmethod
    def get_fail_result_if_exist(cls, results: list['Result']) -> Optional['Result']:
        """리스트에 실패한 결과가 있는 경우, 그 결과를 반환합니다."""
        for result in results:
            if result.is_failure:
                return result
        return None
