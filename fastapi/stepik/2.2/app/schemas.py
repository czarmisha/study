from pydantic import BaseModel


class BaseUser(BaseModel):
    name: str
    age: int


class ResponseUser(BaseUser):
    is_adult: bool
