class BirdDesc:
    def __init__(self, name, type_name):
        self.name = name
        self.type = type_name

    def __set__(self, instance, value):
        if type(value) != self.type:
            raise TypeError(f"Значение должно быть типа {self.type}")
        if self.type is int and value <= 0:
            raise ValueError('Значение атрибута должно быть положительным!')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Невозможно удалить атрибут")


class Bird:
    'Класс для описания птиц'
    wings = 2
    beak = 1
    eyes = 2

    bird_type = BirdDesc('bird_type', str)
    wingspan = BirdDesc('wingspan', int)
    body_length = BirdDesc('body_length', int)
    weight = BirdDesc('weight', int)

    def __init__(self, bird_type, wingspan, body_length, weight):
        # Вид птицы
        self.bird_type = bird_type
        # Размах крыльев в мм
        self.wingspan = wingspan
        # Длина в мм
        self.body_length = body_length
        # Вес в граммах
        self.weight = weight

    def weight_of_flock(self, number_of_birds):
        return self.weight * number_of_birds


bird_1 = Bird('sparrow', 210, 140, 40)
print(bird_1.bird_type)

print(bird_1.__dict__)

bird_2 = Bird('waxwing', 380, 200, 60)
