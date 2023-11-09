from .schemas import UserModel  # , SessionToken

from fastapi import FastAPI, Response, HTTPException, Cookie


app = FastAPI()

_session_token = 'abc123xyz456'  # some session token for test\
fake_user_db = [
    {
        'username': 'user123',
        'password': 'password123',
    },
]


@app.post('/login')
async def login(user: UserModel, response: Response):
    if user.model_dump() in fake_user_db:
        response.set_cookie('session_token', _session_token, secure=True)
        return {'message': "Success loged in"}

    return HTTPException(status_code=401, detail='Not authorized')


@app.get('/user')
async def get_user(session_token=Cookie()):
    if session_token == _session_token:
        return UserModel(**fake_user_db[0])
    
    return HTTPException(status_code=401, detail='Not authorized')
