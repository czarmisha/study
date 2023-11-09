from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    password: str


class SessionToken(BaseModel):
    token: str
