# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(self.speed if self.speed <= 60 else f'Вы движетесь с превышением скорости. Ваша скорость {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(self.speed if self.speed <= 40 else f'Вы движетесь с превышением скорости. Ваша скорость {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    T = TownCar(50, 'green', 'Uber')
    S = SportCar(300, 'red', 'Camaro')
    W = WorkCar(60, 'blue', 'Беларусь')
    P = PoliceCar(20, 'brown', 'УАЗ')

    T.go()
    T.turn('Налево')
    T.show_speed()
    T.stop()

    print('----------------------------------------------------')

    S.go()
    S.turn('Направо')
    S.show_speed()
    S.stop()

    print('----------------------------------------------------')

    W.go()
    W.turn('Налево')
    W.show_speed()
    W.stop()

    print('----------------------------------------------------')

    P.go()
    P.turn('Назад')
    P.show_speed()
    P.stop()
