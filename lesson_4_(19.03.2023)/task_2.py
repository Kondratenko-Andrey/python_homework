"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды
с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за
один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""

import random

number_of_bushes = random.randint(5, 5)
bushes = dict()
for bush in range(1, number_of_bushes + 1):
    bushes[bush] = random.randint(1, 15)

print(bushes)

max_taking = 0
max_taking_bush = 0

for bush in range(2, number_of_bushes):
    temp = bushes[bush] + bushes[bush + 1] + bushes[bush - 1]
    if temp > max_taking:
        max_taking = temp
        max_taking_bush = bush

print(f'Максимально за один заход можно собрать {max_taking} ягод, находясь перед кустом {max_taking_bush}')