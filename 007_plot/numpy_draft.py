import numpy as np

a1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

print(a1)
np_a1 = np.zeros(10)
np_a1[4] = 1
print(np_a1)

np_a1 = np.reshape(np_a1, (-1, 5))
print(np_a1)

np_a2 = np.linspace(10, 49, num=40)
np_a2 = np.flip(np_a2)
print(np_a2)
np_bm2 = np_a2 % 2 == 0
print(np_bm2)
np_a2 = np_a2[np_bm2]
print(np_a2)

np_a3 = np.reshape(np.arange(9, dtype='int32'), (3, 3))
print(np_a3)

np_a4 = np.random.rand(4, 3, 2)
print(np_a4)
print(np.min(np_a4))


np_a5_1 = np.reshape(np.arange(24, dtype = 'int32'), (6, 4))
np_a5_2 = np.reshape(np.arange(12, dtype = 'int32'), (4, 3))
print(np_a5_1)
print(np_a5_2)
np_a5_3 = np_a5_1 @ np_a5_2
print(np_a5_3)

print()
np_a6 = np.random.rand(7, 7)
print(np_a6)
mean_a6 = np.mean(np_a6)
print("mean: ", mean_a6)
std_a6 = np.std(np_a6)
print("std: ", std_a6)
np_a6 = np_a6 / np.linalg.norm(np_a6)
print(np_a6)
