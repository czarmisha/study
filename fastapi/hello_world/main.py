from fastapi import FastAPI
from pydantic import BaseModel
# from typing import Optional
# from fastapi.responses import FileResponse

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get("/", response_class=FileResponse)
# async def root():
#     return 'templates/root.html'


"""
So, with that type declaration,
FastAPI gives you automatic request 'parsing'
"""


@app.get("/root/{item}")  # path parametrs - required
async def root(item: int):
    return {"result": item}


# query parametrs - may be required(if not default value or None)
@app.post("/calculate")
async def calculate(
    required_param: int,
    default_value_param: str = '2',
    not_required_param: str | None = None  # Optional[str] == str | None
):
    return {
        "required_param": required_param,
        "default_value_param": default_value_param,
        "not_required_param": not_required_param,
    }


"""
To send data, you should use one of: POST (the more common),
PUT, DELETE or PATCH.

Sending a body with a GET request has an undefined behavior in
the specifications,nevertheless, it is supported by FastAPI, only for
very complex/extreme use cases.
"""


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return item
