"""
ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ:
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
import random


def fill_list(raw_list, quantity_of_el):
    for i in range(quantity_of_el):
        temp = random.randint(1, 40)
        raw_list.append(temp)


def close_number(source_list, number):
    difference = abs(number - source_list[0])
    close_num = source_list[0]
    for i in range(1, len(source_list)):
        if abs(number - source_list[i]) < difference:
            close_num = source_list[i]
    return close_num


list_1 = list()
flag = True

while flag:
    try:
        n = int(input('Введите количество элементов в массиве: '))
    except ValueError:
        print('Данные введены некорректно, необходимо ввести натуральное число!')
    else:
        flag = False

fill_list(list_1, n)
print(list_1)

flag = True

while flag:
    try:
        x = int(input('Введите число: '))
    except ValueError:
        print('Данные введены некорректно, необходимо ввести целое число!')
    else:
        flag = False

print(f'Cамый близкий по величине элемент из исходного массива к заданному числу: {close_number(list_1, x)}')
