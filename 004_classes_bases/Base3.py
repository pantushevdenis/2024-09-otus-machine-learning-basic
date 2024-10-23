class Human:
    # __slots__ = ('name', 'age', 'work')
    def __init__(self, name, age, work = None):
        self.name = name
        self.age = age
        self.work = work
    def greetings(self):
        print(f'Я тебя приветствую! Меня зовут {self.name}')

    def __str__(self):
        return f'{self.name} {self.work} {self.age}'

human1 = Human('sone', 18, 'otus webinars')
human2 = Human('pietari', 19, 'otus studen')

print(human1.name)
print(human2.name)

human1.name = 'Стоун'
print(human1.name)

human1.greetings()
human2.greetings()

human1.options = 'Опции нашего персонажа' # bad!!!
print(human1.options)

print('print(human1.__dict__)')
print(human1.__dict__)

# print(human2.options) error!!!

human3 = Human('qqq', 10)
print(human3.work)

print(human1)

