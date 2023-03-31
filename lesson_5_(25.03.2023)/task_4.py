"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


class NewClass(Exception):
    pass


def sum_of_el(n):
    sum_el = 1
    if n != 0:
        return sum_el + sum_of_el(n - 1) / -2
    else:
        return 0


flag = True

while flag:
    try:
        num = int(input('Введите кол-во элементов: '))
        if num < 0:
            raise NewClass()
        flag = False
    except ValueError:
        print('Введите целое число!!!')
    except NewClass:
        print('Отрицательное число недопустимо!')

print(f'Количество элементов - {num}, их сумма - {sum_of_el(num)}')
