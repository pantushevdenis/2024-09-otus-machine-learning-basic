class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f'Меня зовут {self.name} и мне {self.age} лет')

    def f2(self):
        pass

class Webinarist(Human):
    def __init__(self, name, age, expirience):
        super().__init__(name, age)
        self.expirience = expirience

    def greetings(self):
        print(f'Меня зовут {self.name} и мне {self.age} лет и я webinarist')


a = Webinarist('stone2', 18, 10)
b = Human('sone1', 14)
print(a)

a.greetings()
b.greetings()

a = [a, b]
for e in a:
    e.greetings()