class MyClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    def __init__(self, value1: int):
        self.value1 = value1

    def __str__(self):
        return f"{self.value1}"

a = MyClass(5)
print(a)


