from pydantic import BaseModel, PositiveInt, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt | None = None
    is_subscribed: bool | None = None
