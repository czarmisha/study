"""
Итераторы — это ключевой концепт в Python, который позволяет создавать и работать с
последовательностями объектов. Они являются основой многих встроенных структур данных,
таких как списки, кортежи и множества, а также используются для создания
пользовательских структур данных.
"""
"""
Итератор — это объект, который реализует два метода: __iter__() и __next__().
Метод __iter__() возвращает сам итератор, а метод __next__() возвращает следующий элемент
в последовательности. Если в последовательности больше нет
элементов, метод __next__() должен вызвать исключение StopIteration.
Пример простого итератора:
"""

class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.max_value:
            self.current_value += 1
            return self.current_value
        else:
            raise StopIteration


my_iter = MyIterator(5)
print(my_iter)
for i in my_iter:
    print(i)


my_iter_obj = iter([1, 2, 3])
print(my_iter_obj)
print(next(my_iter_obj))
print(next(my_iter_obj))
