"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""

import random


def fill_list(raw_list, quantity_of_el):
    for i in range(quantity_of_el):
        temp = random.randint(-10, 10)
        raw_list.append(temp)


flag = True

while flag:
    try:
        n = int(input('Введите количество элементов первого массива: '))
        m = int(input('Введите количество элементов второго массива: '))
    except ValueError:
        print('Данные введены некорректно, необходимо ввести натуральное число!')
    else:
        flag = False

list_1 = list()
list_2 = list()

fill_list(list_1, n)
fill_list(list_2, m)

print(list_1)
print(list_2)

common_elements = set(list_1).intersection(set(list_2))
print(f'Числа, которые встречаютсся в обоих массивах в порядке возрастания: \n {sorted(common_elements)}')
