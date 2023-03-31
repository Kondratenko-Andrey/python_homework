"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


class NewClass(Exception):
    pass


def exponentiation(a, b):
    res = 1
    if b == 0:
        return res
    else:
        return a * exponentiation(a, b - 1)


flag = True
while flag:
    try:
        num_a = int(input('Введите основание степени: '))
        num_b = int(input('Введите показатель степени: '))
        if num_a < 0 or num_b < 0:
            raise NewClass()
        flag = False
    except ValueError:
        print('Введите целое неотрицательное число, а не символы и буквы!')
    except NewClass:
        print('Введите целое неотрицательное число!!!')

print(f'{num_a} ^ {num_b} = {exponentiation(num_a, num_b)}')
