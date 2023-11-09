from .schemas import User

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


app = FastAPI()


sample_products = [
    {
        "product_id": 123,
        "name": "Smartphone",
        "category": "Electronics",
        "price": 599.99
    },
    {
        "product_id": 456,
        "name": "Phone Case",
        "category": "Accessories",
        "price": 19.99
    },
    {
        "product_id": 789,
        "name": "Iphone",
        "category": "Electronics",
        "price": 1299.99
    },
    {
        "product_id": 101,
        "name": "Headphones",
        "category": "Accessories",
        "price": 99.99
    },
    {
        "product_id": 202,
        "name": "Smartwatch",
        "category": "Electronics",
        "price": 299.99
    }
]


@app.post('/user')
async def user_info(user: User) -> User:
    return user


@app.get('/product/{product_id}')
async def get_product(product_id: int):
    for product in sample_products:
        if product['product_id'] == product_id:
            return JSONResponse(product, status_code=200)
    raise HTTPException(status_code=404, detail="Item not found")


@app.get('/products/search')
async def get_product(keyword: str, category: str | None = None, limit: int | None = None):
    pass
