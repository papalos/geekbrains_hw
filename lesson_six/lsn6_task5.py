# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

from tkinter import *


class Stationery:
    title = ''

    def __init__(self):
        self.root = Tk()
        self.root.geometry("850x500+300+300")
        self.root.title(self.title)
        self.canvas = Canvas(self.root, bg="white")
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.bind("<B1-Motion>", self.draw)

    def draw(self, mouse_btn):
        pass


class Pen(Stationery):
    title = 'Ручка'

    def draw(self, mouse_btn):
        self.canvas.create_oval(mouse_btn.x - 2, mouse_btn.y - 2, mouse_btn.x + 2, mouse_btn.y + 2, fill='blue', outline='blue')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self, mouse_btn):
        self.canvas.create_oval(mouse_btn.x - 2, mouse_btn.y - 2, mouse_btn.x + 2, mouse_btn.y + 2, fill='grey', outline='grey')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self, mouse_btn):
        self.canvas.create_oval(mouse_btn.x - 4, mouse_btn.y - 4, mouse_btn.x + 4, mouse_btn.y + 4, fill='yellow', outline='yellow')


if __name__ == '__main__':
    # Раскоментировав одну из строк можно посмотреть как выполняют отрисовку разные объекты,
    # Рисовать зажав левую кнопку мыши
    # app = Pen()
    # app = Pencil()
    app = Handle()
    app.root.mainloop()
