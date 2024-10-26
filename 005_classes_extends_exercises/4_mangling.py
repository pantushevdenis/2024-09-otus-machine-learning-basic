class Sample:
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3

    @property
    def b(self):
        return self._b


s = Sample()
print(s.a)
print(s.b)
# print(s.__c)
print(s._Sample__c)

class Second(Sample):
    def __init__(self):
        super().__init__()
        self.a = 'overriden a'
        self._b = 'overriden b'
        self.__c = 'overriden c'


s2 = Second()
print(s2.a)
print(s2._b)
print(s2._Second__c)
print(s2._Sample__c)

