class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Human(name='stone', age=18)

class Webinarist(Human):
    def __init__(self, name, age, expirience):
        super().__init__(name, age)
        self.expirience = expirience

b = Webinarist('stone2', 18, 10)
print(b)

