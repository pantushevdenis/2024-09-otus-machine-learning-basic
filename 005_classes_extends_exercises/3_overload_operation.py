class MyPair:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def __str__(self):
        return f"{self.value1} <=> {self.value2}"

    def __add__(self, other):
        return MyPair(self.value1 + other.value1, self.value2 + other.value2)


c1 = MyPair(1, 2)
print(c1)

c2 = MyPair(3, 4)
print(c2)

c3 = c1 + c2
print(c3)
