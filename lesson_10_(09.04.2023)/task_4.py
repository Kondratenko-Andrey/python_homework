"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def encode_decode(array):
    for el in array:
        temp_str = el
        temp_str_bytes = temp_str.encode('utf-8')
        print(f'Преобразование объекта "{el}" в тип данных bytes:')
        print(type(temp_str_bytes), temp_str_bytes)

        temp_str = temp_str_bytes.decode('utf-8')
        print(f'Декодирование созданного объекта из bytes в str:')
        print(type(temp_str), temp_str)


my_list = ['разработка', 'администрирование', 'protocol', 'standard']
encode_decode(my_list)
