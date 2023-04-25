"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""


def unicode_converter(word):
    res = word.encode('unicode_escape')
    my_list = list(str(res))
    del my_list[:2]
    del my_list[-1]

    for i in range(len(my_list) - 1):
        if my_list[i] == "\\" and my_list[i + 1] == "\\":
            my_list[i] = '-1'

    for i in range(my_list.count('-1')):
        my_list.remove('-1')

    res = ''.join(my_list)

    return res


my_list = ['разработка', 'сокет', 'декоратор']

for el in my_list:
    my_str = unicode_converter(el)

    print(el, type(el))
    print(my_str, type(my_str))
