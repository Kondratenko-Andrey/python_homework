# ДОПОЛНИТЕЛЬНЫЕ:
# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
# 385916 -> yes
# 123456 -> no

n = int(input('Введите шестизначный номер билета: '))

while n < 100_000 or n > 999_999:
    n = int(input('Номер должен быть шестизначным! Введите шестизначный номер билета: '))

temp_1 = n // 1000  # первая половина номера билета
temp_2 = n % 1000  # вторая половина номера билета

sum_1 = temp_1 // 100 + (temp_1 % 100) // 10 + temp_1 % 10  # сумма цифр первой половины номера билета
sum_2 = temp_2 // 100 + (temp_2 % 100) // 10 + temp_2 % 10  # сумма цифр второй половины номера билета

if sum_1 == sum_2:
    print('Ура! У Вас счастливый билет!')
else:
    print('Увы, билет несчастливый. В следующий раз повезёт.')
