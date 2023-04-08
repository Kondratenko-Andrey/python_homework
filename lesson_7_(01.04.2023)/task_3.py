"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position)
        self._income = income

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        res = self._income['wage'] + self._income['bonus']
        return res

    def __str__(self):
        return f'{self.get_full_name()} {self.position} {str(self.get_total_income())}'


obj = Position('John', 'Wilson', 'Driver', {'wage': 2000, 'bonus': 500})
print(obj.get_full_name())
print(obj.get_total_income())
print(obj)
