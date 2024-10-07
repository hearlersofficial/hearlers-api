# services/user_service/app/domain/models/user.py
from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID
    name: str
    email: str

    def change_email(self, new_email: str):
        self.email = new_email
# 바꿔@@!@!@