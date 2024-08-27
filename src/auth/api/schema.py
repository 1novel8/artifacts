from src.common.dto import BaseDto


class AuthSchema(BaseDto):
    Username: str
    Password: str


class TokenSchema(BaseDto):
    token: str
