# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# К сожалению мне неудалось найти информацию о встроенном переводчике python без использования внешних библиотек
# есть метод translate, но с его помощью возомжно огранизовать только транслитерацию, но не перевод,
# во всяком случае у меня не получилось, буду признателен за информацию
vocabulary = {'One': ['Один', 'I'], 'Two': ['Два', 'II'], 'Three': ['Три', 'III'], 'Four': ['Четыре', 'IV']}

with open('text_4.txt', 'r', encoding='utf-8') as old, open('new_text_4.txt', 'w', encoding='utf-8') as new:
    for i in old:
        words = i.split(' - ')
        translate = vocabulary[words[0]]
        new_str = ' - '.join((translate[0], translate[1]))
        new.writelines((new_str, '\n'))
