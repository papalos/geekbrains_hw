# Создать класс TrafficLight (светофор)
# и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт


# Может не до конца понял задание, но:
# приватный атрибут класса есть,
# метод есть,
# было дозволено использовать tkinter,
# библиотеку time не применял, т.к. она приостанавливает обработку графического окна, интервал задан через рекусивный вызов
# Усложнение задачи вообще не понял, зачем реализовывать проверку порядка, если я его сам задаю? Как он может сбиться?
from tkinter import Tk, Canvas, BOTH


class TrafficLight:
    __color = 'red'

    def __init__(self):
        self._light = {}
        self._time = {'red': 7, 'yellow': 2, 'green': 10}
        self._ls_clr = ['red', 'yellow', 'green']
        self._root = Tk()
        self._root.title('Светофор')
        self._root.geometry("250x250+300+300")
        self._canvas = Canvas()
        self._light['red'] = self._canvas.create_oval(50, 10, 120, 80, outline="gray", width=2)
        self._light['yellow'] = self._canvas.create_oval(50, 90, 120, 160, outline="gray", width=2)
        self._light['green'] = self._canvas.create_oval(50, 170, 120, 240, outline="gray", width=2)
        self._canvas.pack(fill=BOTH, expand=1)

    def blink(self):
        a = self._ls_clr.index(self.__color)
        self._canvas.itemconfigure(self._light[self.__color], fill='')
        a = (a + 1) % 3
        self.__color = self._ls_clr[a]
        self._canvas.itemconfigure(self._light[self.__color], fill=self.__color)
        self._root.after(self._time[self.__color] * 1000, self.blink)

    def running(self):
        self._canvas.itemconfigure(self._light[self.__color], fill=self.__color)
        self._root.after(7000, self.blink)
        self._root.mainloop()


obj = TrafficLight()
obj.running()
