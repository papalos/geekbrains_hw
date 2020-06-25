# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

_dict = {}
with open('text_3.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        key, value = i.replace('\n', '').split(' ')
        try:
            _dict[key] = float(value)
        except ValueError:
            _dict[key] = 0
    print('Не повезло следующим лицам: ')
    count = 0
    _sum = 0
    for n, sal in _dict.items():
        if sal < 20000:
            print(n)
            _sum += sal
            count += 1
    print('Их средняя зарплата составляет: ', round(_sum/count, 2))

