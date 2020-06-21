# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

ls = list(range(100, 1001, 2))
# На случай если list не использует возможности генератора
ls_2 = [x for x in range(100, 1001, 2)]
# На случай если во втором варианте были использованы не все возможности генератора
ls_3 = [x for x in range(100, 1001) if not x % 2]
print(ls)
print(ls_2)
print(ls_3)

# Надеюсь я правильно полнял задание
print(reduce(lambda x, y: x*y, ls))
