class Human:
    def __init__(self, name, age, pf):
        self._name = name
        self._age = age
        self.__pf = pf

    def greetings(self):
        print(f'Меня зовут {self._name} и мне {self._age} лет')

    def f2(self):
        pass

class Webinarist(Human):
    def __init__(self, name, age, pf, expirience):
        super().__init__(name, age)
        self.expirience = expirience

    def greetings(self):
        print(f'Меня зовут {self._name} и мне {self._age} лет и я webinarist')


a = Webinarist('stone2', 18, 'rr', 10)

b = Human('sone1', 14, 'tt')
print(a)

a.greetings()
b.greetings()

a = [a, b]
for e in a:
    e.greetings()