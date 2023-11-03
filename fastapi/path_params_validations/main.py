"""
Так же как мы можем добавить доплнительную валидацию в query params
с помощью Query, мы можем добавить валидация к path params с помошью Path
"""

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('items/{item_id}')  # Обычный параметр пути
async def get_item(item_id: int):
    results = {"item_id": item_id}
    return results


@app.get('items2/{item_id}')  # Параметр пути с дополнительными параметрами
async def get_item2(item_id: Annotated(int, Path(title="The ID of the item to get"))):
    results = {"item_id": item_id}
    return results


"""
Ну для строк были max_length и тд, для чисел есть ge (>=), le (<=), gt, lt
Для float тоже буду работать
"""