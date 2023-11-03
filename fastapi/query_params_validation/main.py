from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()
"""
Мы можем дополнительно валидировать Query params в url
Типа не только тип данных :str, а еще и например максимальную длину 
"""


@app.get('/items/')  # это простой query param. валидация по типу
async def get_items(q: str | None = None):  # и он не обязателен
    return {"query param": q}


"""
Annotated
Сам питон ничего с ним не делает, как и со всеми другими типизациями
FastAPI использует Annotated чтобы мы могли передать какие-то дополнительные мета данные
Первый параметр Annotaed это настоящие фактические типы, все остальное это какие-то мета данные для
    других инструментов таких как FastAPI

Query
Он короче говорит что параметр - параметр строки (querry params которые после ? в url)
Короче у него есть аргументы типа max_length, pattern(re), decimal_places которые добавляют
    дополнительную валидацию параметра
"""
@app.get('/items/validate/')
async def get_items_validated(q: Annotated[str | None, Query(max_length=5)] = None):
    return {"query param": q}
