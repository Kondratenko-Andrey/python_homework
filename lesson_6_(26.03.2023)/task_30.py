"""
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""


class NewClass(Exception):
    pass


flag = True
while flag:
    try:
        a_1 = int(input('Введите первый элемент арифметической прогрессии: '))
        d = int(input('Введите разность между соседними элементами: '))
        n = int(input('Введите количество элементов арифметической прогрессии: '))
        if n < 0:
            raise NewClass()
        flag = False
    except ValueError:
        print('Некорректный ввод данных!!')
    except NewClass:
        print('Некорректный ввод данных!!')

my_list = [a_1 + (el - 1) * d for el in range(a_1, n + 1)]
for el in my_list:
    print(el)
