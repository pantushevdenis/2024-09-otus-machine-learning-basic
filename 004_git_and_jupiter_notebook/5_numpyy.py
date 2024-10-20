import numpy as np

a = np.random.rand(10)
print(a)

min_element = np.min(a)
max_element = np.max(a)

print(min_element)
print(max_element)
a[a <= min_element] = 0.0
a[a >= max_element] = 1.0

print(a)

arr1 = np.random.randint(0, 50, size = (5, 6))
print(arr1)
r = np.argmax(arr1.max(axis = 0))
print(r)



