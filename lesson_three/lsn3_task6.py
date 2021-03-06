# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


# Странно видеть в названии функции int_ если она принимает и возвращает строку, но раз того требует задание
def int_func(text: str):
    return text.capitalize()


# Продолжение задания можно было бы не делать если в разарбатываемой версии функции int_func(text: str)
# использовать строковый метод .title(), но видимо этого нельзя делать, или я не понял задание
def super_str(text: str):
    ls = list(text.split(' '))
    new_str = ' '.join(map(int_func, ls))
    return new_str


print(super_str(input('Введите строку из слов в нижнем регистре, разделенных пробелом: ')))
