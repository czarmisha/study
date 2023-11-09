from fastapi import FastAPI
from .schemas import BaseUser, ResponseUser


app = FastAPI()


@app.post('/user')
def adult_check(user: BaseUser) -> ResponseUser:
    is_adult = True if user.age >= 18 else False
    response_user = ResponseUser(**user.model_dump(), is_adult=is_adult)
    return response_user
