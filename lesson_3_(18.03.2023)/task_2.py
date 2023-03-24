"""
БАЗОВЫЕ ЗАДАНИЯ:
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def num_division(num_1, num_2):
    try:
        res = num_1 / num_2
    except ZeroDivisionError:
        print('На ноль делить нельзя! Значение частного не определено!')
    else:
        return res


flag = True

while flag:
    try:
        n_1 = int(input('Введите первое число: '))
        n_2 = int(input('Введите второе число: '))
    except ValueError:
        print('Данные введены некорректно, необходимо ввести целые числа!')
    else:
        flag = False

print(f'{n_1} / {n_2} = {num_division(n_1, n_2)}')
