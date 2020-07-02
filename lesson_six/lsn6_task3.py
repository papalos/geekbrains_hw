# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.surname + " " + self.name

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


if __name__ == '__main__':
    a = Position('Иван', 'Иванов', 'Раб', 10, 0)
    b = Position('Марсель', 'Кац', 'Плантатор', 10000, 100000)
    print(a.get_full_name())
    print(a.get_total_income())
    print(b.get_full_name())
    print(b.get_total_income())
