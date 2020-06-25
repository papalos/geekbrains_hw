# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

_dict = {}
with open('text_7.txt', 'r', encoding='utf-8') as f:
    for _str in f:
        ls = _str.replace('\n', '').split(' ')
        # Исходя из примера прибыль целочисленная
        _dict[ls[0]] = int(ls[2]) - int(ls[3])

ls_average_profit = [x for x in _dict.values() if x > -1]
num_average_profit = sum(ls_average_profit)/len(ls_average_profit)
ls = [_dict, {'average_profit': num_average_profit}]
print(_dict)
print(ls_average_profit)
print(num_average_profit)
print(ls)

with open("json.json", "w", encoding='utf-8') as f_json:
    json.dump(ls, f_json, ensure_ascii=False, indent=2)
