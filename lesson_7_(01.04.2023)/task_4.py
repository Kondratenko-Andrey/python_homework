"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""

from random import randint


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        res = ''
        for i in self.list_of_lists:
            res += (' '.join(map(str, i))) + '\n'
        return res

    def __add__(self, other):
        res = [[self.list_of_lists[j][i] + other.list_of_lists[j][i] for i in range(5)] for j in range(4)]
        return Matrix(res)


my_list = [[randint(-10, 10) for i in range(5)] for j in range(4)]
my_list_2 = [[randint(-10, 10) for el in range(5)] for arr in range(4)]

obj_1 = Matrix(my_list)
obj_2 = Matrix(my_list_2)

print(obj_1)
print(obj_2)

print(obj_1 + obj_2)
