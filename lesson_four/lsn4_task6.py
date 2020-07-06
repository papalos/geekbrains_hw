# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


# !!!!!!! Очень прошу разъяснения, что значит скрипт итератор???
# Ведь итератор это как минимум объект способный перебирать значения итерируемого объекта,
# как максимум патерн реализуемый подобным образом.
# Если в задании требуется просто использовать функции count() и cycle() возвращающие итераторы, тогда решение ниже:
from itertools import count, cycle


def step_by_step(init):
    for i in count(init):
        if i > 20:
            break
        else:
            print(i)


def again(_list):
    i = 0
    for el in cycle(_list):
        if i > 20:
            break
        print(el)
        i += 1


step_by_step(3)
again('sdfdsf')


# Если же необходимо создавать объект итератор, тогда решение может выглядеть как-то так
class StepByStep:
    def __init__(self, init):
        self.counter = init
        self.stop = 20

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.stop + 1:
            self.counter += 1
            return self.counter - 1
        else:
            raise StopIteration


for i in StepByStep(3):
    print(i)


class Again:

    def __init__(self, init_ls):
        self.ls = init_ls
        self.num_step = 0
        self.stop = 20
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > len(self.ls)-1:
            self.counter = 0
        if self.num_step < self.stop:
            self.counter += 1
            self.num_step += 1
            return self.ls[self.counter-1]
        else:
            raise StopIteration


for i in Again('ABC'):
    print(i)
