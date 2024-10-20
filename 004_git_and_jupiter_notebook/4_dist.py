import numpy as np


a = np.random.randint(-10, 10, size=10)
print(a)
b = np.random.randint(-10, 10, size=10)
print(b)
s = np.subtract(a, b)
print(s)
sq = np.square(s)
print(sq)
summ = np.sum(sq)
print(summ)
d = np.sqrt(summ)
print(d)

abs = np.abs(s)
print(abs)
