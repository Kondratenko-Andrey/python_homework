"""
ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ:
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""
import random


def fill_list(raw_list, quantity_of_el):
    for i in range(quantity_of_el):
        temp = random.randint(1, 10)
        raw_list.append(temp)


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
        x = int(input('Введите одно из значений элементов сформированного массива: '))
    except ValueError:
        print('Данные введены некорректно, необходимо ввести целое число!')
    else:
        flag = False

if list_1.count(x) == 0:
    print(f'Элемент с введенным Вами значением {x} отсутствует в исходном массиве')
else:
    print(f'Количество элементов со значением {x} в исходном массиве: {list_1.count(x)}')
