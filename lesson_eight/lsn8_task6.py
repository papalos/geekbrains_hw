# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


from lsn8_task5 import Storage


class OwnError(Exception):
    msg = 'Количество оборудования может быть только положительным числом!'


def to_number(x: str):
    if x.isdigit():
        return int(x)
    else:
        raise OwnError


stg = Storage()

while True:
    print('Выберите операцию:')
    print('1 - поступление на склад')
    print('2 - перемещение оборудования в офис')
    print('3 - аудит')
    print('4 - выход')

    i = int(input())
    if i == 1:
        t = input('Введите тип оборудования: ')        # (принтер, сканер, ксерокс)
        if stg.type_eq.get(t):
            try:
                n = to_number(input('Введите количество единиц оборудования: '))
                for i in range(n):
                    stg.get_equipment(t)
                continue
            except OwnError as e:
                print(e.msg)
                continue
        else:
            print('Такой тип оборудования не храниться на этом складе')
            continue
    if i == 2:
        t = input('Введите тип оборудования: ')  # (принтер, сканер, ксерокс)
        if stg.type_eq.get(t):
            stg.move_equipment(t)
            continue
    if i == 3:
        stg.revision_eq()
        continue
    if i == 4:
        break
    print('Операция недоступна')

print('Конец работы')
