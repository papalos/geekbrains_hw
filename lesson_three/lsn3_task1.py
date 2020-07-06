# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def get_nums(score):
    n = []
    while True:
        try:
            i = int(input('Введите число: '))
            n.append(i)
            if len(n) == score:
                return n
        except ValueError:
            print('Вы ввели не число!')


# Основная функция требуемая в задании
def two_div(x, y):
    try:
        return x / y
    except ZeroDivisionError as err:
        return 'Деление на ноль запрещено!'


# Тут распаковака, но передача аргументов как по условию - позиционно
print(two_div(*get_nums(2)))
