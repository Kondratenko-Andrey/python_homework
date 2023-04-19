class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.a = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.a is None:
            self.a = super().__call__(*args, **kwargs)
            return self.a
        else:
            return self.a


class MyClass(metaclass=Singleton):
    def __init__(self, a_1, a_2):
        self.atr_1 = a_1
        self.atr_2 = a_2


obj_1 = MyClass(10, 12)
obj_2 = MyClass('a', 'b')
obj_3 = MyClass('z', 16)

print(obj_1 is obj_2)
print(obj_2 is obj_3)
print(obj_1 is obj_3)

print(obj_1)
print(obj_2)
print(obj_3)

print(obj_1.__dict__)
print(obj_2.__dict__)
print(obj_3.__dict__)
