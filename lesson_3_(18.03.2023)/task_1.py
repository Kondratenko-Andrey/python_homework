"""
БАЗОВЫЕ ЗАДАНИЯ:

1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

import random

seasons_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето',
                'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
seasons_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
                7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
num_of_month = random.randint(1, 12)

print(f'Заданный номер месяца: {num_of_month}')
print(f'Результат через список: {seasons_list[num_of_month - 1]}')
print(f'Результат через словарь: {seasons_dict[num_of_month]}')
