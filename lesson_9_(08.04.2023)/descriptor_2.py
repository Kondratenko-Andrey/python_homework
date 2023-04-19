class UserDesc:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if self.name == "email" and "@" and '.' not in value:
            raise ValueError('email введён некорректно!')
        if self.name == "reg_year" and not 2020 <= value <= 2023:
            raise ValueError('Год регистрации указан некорректно!')
        instance.__dict__[self.name] = value


class User:
    name = UserDesc()
    email = UserDesc()
    password = UserDesc()
    reg_year = UserDesc()

    def __init__(self, user_name, user_email, user_password, year_of_registration):
        self.name = user_name
        self.email = user_email
        self.password = user_password
        self.reg_year = year_of_registration


obj = User('Andrew', 'andrey92kondr@gmail.com', 1234, 2023)

print(obj.__dict__)
