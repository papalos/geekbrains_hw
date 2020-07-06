# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.


while True:
    start = int(input('Сколько спортсмен способен пробежать в первый день? '))
    if start > 0:
        break
    print('Расстояние должно быть положительным числом. Введите корректные данные')

while True:
    finish = int(input('Какого результата необходимо достичь спортсмену? '))
    if start < finish:
        break
    print('Итоговый результат должен быть больше начальных достижений. Введите корректные данные')

step = start
day = 1
while step < finish:
    print(f'{day}-й день: {step:.2f}')
    step += step/10
    day += 1

print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {finish} км.')