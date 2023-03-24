# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import random

peters_num1 = random.randint(1, 1000)
peters_num2 = random.randint(1, 1000)

print(peters_num1, peters_num2)

s = peters_num1 + peters_num2
p = peters_num1 * peters_num2
flag = True

for i in range(1, 1001):
    for j in range(1, 1001):
        if i + j == s and i * j == p and flag:
            print(f'Катя отгадала задуманные числа, они равны {i} {j}')
            flag = False
