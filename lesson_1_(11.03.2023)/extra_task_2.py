# ДОПОЛНИТЕЛЬНЫЕ:
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input(
    'Введите целое положительное число, кратное 6 (в соответствии с условием задачи и во '
    'избежании дробной части журавлика): '))

while s % 6:
    print('Некорректный ввод данных!')
    s = int(input('Введите целое положительное число, кратное 6: '))

pet_ser = s // 6  # кол-во журавликов, которое сделал Петя или Сережа
kate = 2 * (pet_ser + pet_ser)  # кол-во журавликов, которое сделала Катя

print(f'Количество журавликов, которое сделал Петя равно: {pet_ser}')
print(f'Количество журавликов, которое сделал Серёжа равно: {pet_ser}')
print(f'Количество журавликов, которое сделала Катя равно: {kate}')
