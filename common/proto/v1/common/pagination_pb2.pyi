from v1.common import sort_order_pb2 as _sort_order_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Pagination(_message.Message):
    __slots__ = ("sort_order", "since", "limit")
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    sort_order: _sort_order_pb2.SortOrder
    since: str
    limit: int
    def __init__(self, sort_order: _Optional[_Union[_sort_order_pb2.SortOrder, str]] = ..., since: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...
