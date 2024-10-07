
from common.core.message.query.base_query import BaseQuery


class GetUserQuery(BaseQuery):
    def __init__(self, id: str):
        self.id = id
