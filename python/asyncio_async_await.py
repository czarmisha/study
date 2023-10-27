# pip install aiohttp
import asyncio
import inspect


# "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
@asyncio.coroutine  # из функции создают корутины на основе генераторов
def test():
    print('Hello world!')


print(inspect.isgeneratorfunction(test))  # True
g = test()
try:
    next(g)
except StopIteration:
    pass


async def print_nums():
    num = 0
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds have passed')
        count += 1
        await asyncio.sleep(1)

 
async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())

