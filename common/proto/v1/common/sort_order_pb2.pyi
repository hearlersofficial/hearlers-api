from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_ORDER_UNSPECIFIED: _ClassVar[SortOrder]
    SORT_ORDER_ASC: _ClassVar[SortOrder]
    SORT_ORDER_DESC: _ClassVar[SortOrder]
    SORT_ORDER_BOTH: _ClassVar[SortOrder]
SORT_ORDER_UNSPECIFIED: SortOrder
SORT_ORDER_ASC: SortOrder
SORT_ORDER_DESC: SortOrder
SORT_ORDER_BOTH: SortOrder
