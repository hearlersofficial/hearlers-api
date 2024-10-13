
from pydantic import BaseModel

from common.enum.user.auth_channel import AuthChannel


class LoginRequest(BaseModel):
    code: str
    state: str
    authChannel: AuthChannel