# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

flag = False
n = input('Введите число: ')

if int(n) < 0:
    flag = True
    n = int(n)
    n = str(-n)

_sum = int(n) + int(n*2) + int(n*3)

if True:
    _sum *= -1

print(_sum)