"""
coroutines/сопрограммы - генераторы которые в процессе работы могут принимать извне какие-то данные.
Делается это с помощью метода generator.send() или next(generator)
"""

from inspect import getgeneratorstate
def subgen():
    message = yield
    print('Received message: ', message)

gen = subgen()  # create a generator object
# gen.send('test test')  # exception! can send only None in just created generator
print(getgeneratorstate(gen))  # GEN_CREATED

gen.send(None)  # сдвигаем управления до следующего yield
print(getgeneratorstate(gen))  # GEN_SUSPENDED

try:
    gen.send('test message')
except StopIteration:
    pass

print('\n\ngen2:')
"""
1 - yield отдает значения. вверху yield как бы отдал нам None
2 - yield получает значения через метод send()
"""

def subgen2():
    x = 'Ready to reicive message'
    message = yield x
    print('Received message: ', message)

gen2 = subgen2()
yielded_mess = gen2.send(None)  # return x from generator
print(yielded_mess)

try:
    gen2.send('let\'s go')  # put sended message to message variable and print()
except StopIteration:
    pass



print('\n\ngen3:')
"""
----------------------------------------------------------------------
попробуем сделать генератор которые принимает какое то число(например оценку за день)
и возвращает среднюю оценку за все время
"""

def average():
    count = 0
    summ = 0
    average = None

    while True:
        mark = yield average  # сюда можно передать даже exception например чтобы завершить действие. тут же его ловить try except. !! делается это generator.throw(exception)
        count += 1
        summ += mark
        average = round(summ / count, 2)


gen3 = average()
gen3.send(None)  # сдвинулись до yield(по идее получили average, но оно вначале None)
average = gen3.send(2)
print(average)
average = gen3.send(5)
print(average)
average = gen3.send(2)
print(average)


print('\n\ngen4:')
"""
постоянно сдвигать при создании генератора не удобно .send()
можно создать для этого декоратор
"""

def coroutine(func):
    def wrapper(*args, **kwargs):
        generator = func(*args, **kwargs)
        generator.send(None)
        return generator
    return wrapper


@coroutine
def average2():
    count = 0
    summ = 0
    average = None

    while True:
        mark = yield average  # сюда можно передать даже exception например чтобы завершить действие. тут же его ловить try except. !! делается это generator.throw(exception)
        count += 1
        summ += mark
        average = round(summ / count, 2)


gen4 = average2()
print(getgeneratorstate(gen4))
average = gen4.send(5)
print(average)


print('\n\ngen5:')
"""
Генераторы могут возвращать одно значение с помощью return, но есть особенности.
Если мы не хотим каждую итерацию возвращать среднее занчения, а например накопить его и потом вернуть 1 раз.
Значение return мы можем получить только перехватив исключение StopIteration и посмотреть на него StopIteration.value
"""

@coroutine
def average3():
    average = None
    count = 0
    sum = 0

    while True:
        try:
            x = yield
        except StopIteration:
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)
    return average


gen = average3()
gen.send(1)
gen.send(2)
gen.send(3)
try:
    gen.throw(StopIteration)
except StopIteration as e:
    print('Average: ', e.value)




print('\n\ndelegator/subgenerator')
# Делегирующий генератор и подгенератор
"""
Делегирующий генератор - это генератор который вызывает другой генератор(подгенератор)
Подгенератор - вызываемый другим генератором

"""


def subgen():
    for i in 'Mikhail':
        yield i


def delegator(gen):
    for i in gen:
        yield i


subg = subgen()
gen = delegator(subg)
print(next(gen))
print(next(gen))
print(next(gen))


"""Превратим генераторы в корутины"""
@coroutine
def subgen():
    while True:
        try:
            mess = yield
        except StopIteration:
            print('KUKU')
            break
        else:
            print('-------', mess)


@coroutine
def delegator(gen):
    while True:
        try:
            data = yield
            gen.send(data)
        except StopIteration as e:
            gen.throw(e)
            break


sg = subgen()
deleg = delegator(sg)
print(deleg.send('Ok'))
try:
    deleg.throw(StopIteration)
except:
    pass


"""
можно короче сократить все это с помощью yield from в дерегирующем генераторе
"""

# если посмотреть на спецификацию yield from (pep 380) - он сам внутри проводит инициализаций подгенератора.
# поэтому я убрал декоратор @coroutine
def subgen():
    while True:
        try:
            mess = yield
        except StopIteration:
            print('KUKU')
            break
        else:
            print('-------', mess)


@coroutine
def delegator(gen):
    yield from gen


sg = subgen()
deleg = delegator(sg)
print(deleg.send('Ok'))
try:
    deleg.throw(StopIteration)
except:
    pass

# прикол в том что делегтор может получать от подгенератора значения из return не обрабатывая исключения

def subgen():
    while True:
        try:
            mess = yield
        except StopIteration:
            print('KUKU')
            break
        else:
            print('-------', mess)
    return "REturnred from subgenerator"


@coroutine
def delegator(gen):
    result = yield from gen
    print(result)


sg = subgen()
deleg = delegator(sg)
print(deleg.send('Ok'))
try:
    deleg.throw(StopIteration)
except:
    pass



# yield from в других языках называется await
# делегирующий генератор заблокирован пока ждет подгенератор
"""
def a():
    yield from 'Mikle'
"""
