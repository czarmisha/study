"""
попробуем скачать 10 рандомных картинок с url https://loremflickr.com/320/240
попробуем сделать синхронно и асинхронно и сравнить время
"""

import requests
from time import time
import asyncio  # предоставляет api для работы с протоколами udp и tcp/ но api для работы с http у него нет
import aiohttp  # поэтому ставим библу для работы с http


url = 'https://loremflickr.com/320/240'


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f'Synch execution time is {end-start}')
    return wrapper


def get_file(url):
    res = requests.get(url, allow_redirects=True)
    return res


def write_file(response):
    # https://loremflickr.com/cache/resized/65535_52556072582_d5e25f27cf_z_320_240_nofilter.jpg
    filename = response.url.split('/')[-1]
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


@timer
def main_sync():
    for i in range(10):
        write_file(get_file(url))


# по документации aiohttp все запросы лучше делать через созданную сессию
async def fetch_content(url, session):
    # с сессией обычно работают через контекстный менеджер
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def write_image(data):
    filename = f'file-{int(time() * 1000)}.jpg'
    with open(filename, 'wb') as file:
        file.write(data)  # asyncio не работает синхронно с файлами


def atimer(func):
    async def wrapper(*args, **kwargs):
        start = time()
        await func(*args, **kwargs)
        end = time()
        print(f'Async execution time is {end-start}')
    return wrapper


@atimer
async def main_async():
#    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
 #           tasks.append(tasks)
            await task

#            await asyncio.gather(*tasks)


if __name__ == '__main__':
    main_sync()
    asyncio.run(main_async())
