'''
Декораторы в Python — это мощный инструмент, который позволяет модифицировать поведение
функций или классов без изменения их кода. Они представляют собой функции высшего порядка,
то есть функции, которые принимают другие функции в качестве аргументов и возвращают новые
функции. В Python декораторы обычно применяются с помощью синтаксиса @decorator перед
определением функции или класса.
https://sky.pro/media/chto-takoe-dekoratory-v-python/
'''

import time


def my_decorator(func):  # decorator function
    def wrapper(*args, **kwargs):  # wrapper function
        print('doing something before main func')
        func(*args, **kwargs)  # замыкание - доступ к переменным внешней функциии
        print('doing something after main func')
    return wrapper  # required to return wrapper function


# сахар питона
@my_decorator
def say_hello(name='Mikle'):
    print(f"Hello {name}")


say_hello(name='World')
print('\n')


def say_hello2(name='Mikle'):
    print(f"Hello {name}")


# можно и так
decorate_func = my_decorator(say_hello2)
decorate_func('World')
print('\n')



'''we can user multiple decorators for function'''
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения функции: {end_time-start_time}')
    return wrapper


@time_decorator  # первым выполнится my_decorator, потом уже time_decorator вокруг первого
@my_decorator
def sum_nums(x, y):
    print(x+y)


sum_nums(2, 3)
print('\n\n')


''' Иногда нужно передавать параметры в декоратор. используем замыкание и добавим 
еще одну внешнюю функцию. Справа от знака собачки (@) в синтаксисе декоратора должен стоять какой-то вызываемый
объект (т.е. тот, который можно вызвать как функцию), короче нечто foo, которое будет вызвано, как foo(f) в
процессе декорации, где f – декорируемая функция. Под это описание попадают:
- имя функции
- переменная, которой присвоена функция
- экземпляр класса, у которого реализован __call__
- или собственно функциональный вызов func(...), который вернет что-то тоже вызываемое из списка выше

то есть при вызове @decorator(*args, **kwargs) вернется тоже вызываемый элемент который и будет декоратором @(result of decorator(args))
@decorator(param=42)
def foo(x, y):
    return x + y
Эквивалентно примерно этому:
foo = decorator(param=42)(foo)
или
pure_decorator = decorator(param=42)
foo = pure_decorator(foo)

https://tirinox.ru/parametric-decorator/
'''


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(5)
def say_hi():
    print('Hi!')


say_hi()



'''
пример докораторов классов
'''
def add_new_method(class_to_decorate):
    class DecoratedClass(class_to_decorate):
        def new_method(self):
            return "This is a new method"
    return DecoratedClass
 
@add_new_method
class MyClass:
    def my_method(self):
        return "This is my method"
 
my_object = MyClass()
print(my_object.my_method())  # вывод: This is my method
print(my_object.new_method())  # вывод: This is a new method
