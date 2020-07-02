# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


# Ниже приведен абстрактный класс, а не интерфейс, т.к. того требует задание
class AbstractCount(ABC):
    _value = 0

    # @property здесь используется как проверка на ввод числа при создании класса,
    # если ввести другой символ будет поднято стандартное исключение
    # Просто мысли в слух:
    # поля хранят значения, методы их получают или возвращают, на кой огород городить с этими свойствами
    # Один из пунктов манифеста Python гласит: Простое лучше, чем сложное. :-)))
    def __init__(self, measure):
        self.value = measure

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, m):
        self._value = int(m)

    @abstractmethod
    def material(self):
        ...


class Suit(AbstractCount):
    def __init__(self, i):
        super().__init__(i)
        self.V = super().value

    def material(self):
        return self.V / 6.5 + 0.5


class Coat(AbstractCount):
    def __init__(self, i):
        super().__init__(i)
        self.H = super().value

    def material(self):
        return 2 * self.H + 0.3


class Clothes:
    def __init__(self):
        self._clothes = []

    def make_coat(self, size):
        self._clothes.append(Coat(size))

    def make_suit(self, height):
        self._clothes.append(Suit(height))

    # По заданю не понятен формат вывода, предположим метод будет выводить размер в квадратных метрах ввиде числового значения
    def count_material(self):
        return round(sum([c.material() for c in self._clothes]), 2)


if __name__ == '__main__':
    Cl = Clothes()
    Cl.make_coat(34)
    Cl.make_coat(56)
    Cl.make_suit(156)
    Cl.make_suit(183)
    print(Cl.count_material())
