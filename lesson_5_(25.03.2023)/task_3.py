"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


class NewClass(Exception):
    pass


def reverse_num(num):
    if num < 10:
        print(num, end='')
    else:
        print(num % 10, end='')
        reverse_num(num // 10)


flag = True

while flag:
    try:
        number = int(input('Введите положительное целое число: '))
        if number <= 0:
            raise NewClass()
        flag = False
    except ValueError:
        print('Вы ввели не число!')
    except NewClass:
        print('Необходимо ввести положительное число!!')

print(f'Цифры введённого Вами числа в обратном порядке: ', end='')
reverse_num(number)