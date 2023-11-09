from fastapi import FastAPI, Depends, status, HTTPException, Response
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()


class User(BaseModel):
    username: str
    password: str


user_data = {
    "user1": User(**{"username": "user1", "password": "pass1"}),
    "user2": User(**{"username": "user2", "password": "pass2"})
}


def get_user(username: str) -> User | None:
    if username in user_data:
        return user_data[username]
    return None


def authenticate(credentials: HTTPBasicCredentials = Depends(security)) -> User:
    user = get_user(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    return user


@app.get("/login")
def login(user: User = Depends(authenticate)):
    response = Response(content='{"message": "You got my secret, welcome"}')
    response.headers["WWW-Authenticate"] = "Basic, no-store"
    response.status_code = status.HTTP_202_ACCEPTED
    return response