# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def person(name, surname, date, city, email, phone):
    return ' '.join((surname, name, date, email, phone, city))


print(person(surname='Иванов', name='Иван', date='22.02.2002', city='Лондон', email='i@a.com', phone='+78596236532'))