from fastapi import FastAPI, Query, Path, Body
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    name: str
    full_name: str | None = None


@app.post('/items/{item_id}')
async def create_item(item_id: int, item: Item, q: str | None = None):
    results = {"item_id": item_id, "item": item}
    if q:
        results.update(q=q)
    return results
"""
от кода сверху мы ожидаем примерно вот такой body json
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
"""

# Мы также может передавать в агременты несколько body переменных
@app.post('/items2/{item_id}')
async def create_item2(item_id: int, item: Item, user: User, q: str | None = None):
    results = {"item_id": item_id, "item": item}
    if q:
        results.update(q=q)
    return results
"""
от кода сверху мы ожидаем примерно вот такой body json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
FastAPI будем искать название агрумента Pydantic модели как ключ в body json
"""

# чтобы передать единственное значение
@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
"""
от кода сверху мы ожидаем примерно вот такой body json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
"""

# при embed=True будет вот так
@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
"""
от кода сверху мы ожидаем примерно вот такой body json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
вместо этого
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}

"""