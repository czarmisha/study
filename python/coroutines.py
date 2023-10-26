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
