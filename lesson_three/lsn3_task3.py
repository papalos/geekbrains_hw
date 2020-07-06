# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def get_nums(score):
    """
        score: int - количество элементов требуеммых для ввода
        return n: list - список корректно введенных переменных
    """
    n = []
    while True:
        try:
            i = int(input('Введите число: '))
            n.append(i)
            if len(n) == score:
                return n
        except ValueError:
            print('Вы ввели не число!')


# Реализация функции требуемой в задании
def my_func(a, b, c):
    ls = sorted((a, b, c))
    return ls[0] + ls[1]


# Аналогично первому заданию
print(my_func(*get_nums(3)))
