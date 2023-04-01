"""
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
больше заданного максимума)
"""

from random import randint

min_value = -5
max_value = 5

my_list = [randint(-25, 25) for el in range(15)]
print(my_list)

my_dict = {my_list.index(el): el for el in my_list if min_value <= el <= max_value}
print(my_dict)
