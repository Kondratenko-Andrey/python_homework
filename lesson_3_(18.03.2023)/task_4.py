"""
БАЗОВЫЕ ЗАДАНИЯ:
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

import random


def my_func_1(var_1, var_2, var_3):  # функция с использованием sort()
    list_1 = [var_1, var_2, var_3]
    list_1.sort()
    sum_of_max_el = list_1[-1] + list_1[-2]
    return sum_of_max_el


def my_func_2(var_1, var_2, var_3):  # функция без использования sort()
    list_1 = [var_1, var_2, var_3]
    sum_of_max_el = 0

    for j in range(2):
        max_el = list_1[0]
        for i in list_1:
            if i > max_el:
                max_el = i
        sum_of_max_el += max_el
        list_1.remove(max_el)

    return sum_of_max_el


num_1 = random.randint(1, 100)
num_2 = random.randint(1, 100)
num_3 = random.randint(1, 100)

print(f'Исходные три числа: {num_1}, {num_2}, {num_3}')
print(f'Сумма двух наибольших из трёх чисел (вызвана my_func_1): {my_func_1(num_1, num_2, num_3)}')
print(f'Сумма двух наибольших из трёх чисел (вызвана my_func_2): {my_func_2(num_1, num_2, num_3)}')
