# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].


# Вот опять не понятно условие, почему в результирующий список примера не попадает число 300,
# ведь по идее значение Нулевого элемента сравнивается со значением предыдущено Минус первого элемента,
# который по сути является последним в списке. Если бы небыло примера вывода я бы упустил этот момент.
a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = [x for i, x in enumerate(a) if x > a[i-1] and i != 0]
print(b)
