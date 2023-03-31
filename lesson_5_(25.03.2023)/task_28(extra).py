"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4
"""


class NewClass:
    pass


def sum_a_b(a, b):
    if b == 0:
        return a
    else:
        return sum_a_b(a + 1, b - 1)


flag = True
while flag:
    try:
        num_a = int(input('Введите первое слагаемое: '))
        num_b = int(input('Введите второе слагаемое: '))
        if num_a < 0 or num_b < 0:
            raise NewClass()
        flag = False
    except ValueError:
        print('Введите целое неотрицательное число, а не символы и буквы!')
    except NewClass:
        print('Введите целое неотрицательное число!!!')

print(f'{num_a} + {num_b} = {sum_a_b(num_a, num_b)}')
