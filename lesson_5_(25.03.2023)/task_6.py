"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


class NewClass(Exception):
    pass


def my_func(num, count=10):
    if count == 0:
        return print(f'Вы использовали все десять попыток и не угадали число, загаданное число: {num}')

    flag = True
    while flag:
        try:
            user_num = int(input('Угадайте число: '))
            if user_num < 0 or user_num >= 100:
                raise NewClass()
            flag = False
        except ValueError:
            print('Введите целое число, а не буквы и символы!')
        except NewClass():
            print('Число должно быть от нуля, до ста')

    if user_num < num:
        print('Число, которые вы написали, меньше загаданного!')
        return my_func(num, count - 1)

    elif user_num > num:
        print('Число, которые вы написали, больше загаданного!')
        return my_func(num, count - 1)

    elif user_num == num:
        return print(f'УРА!!! Вы угадали! Загаданное число: {num}')


print('Загадано число от 0 до 100. Попытайтесь угадать, у Вас 10 попыток!')

my_func(randint(0, 99))
# my_func(65)
