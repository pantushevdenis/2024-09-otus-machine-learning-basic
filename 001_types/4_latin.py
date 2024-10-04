# Пользователь вводит целое положительное число, программа должна вернуть строку в виде римского числа
# Пример:
# 3 -> III
# 15 -> XV
# 3 234 -> CCXXXIV
from builtins import divmod

# input data
# decimal = 436
decimal = int(input("Введите целое положительное число: "))
assert 0 < decimal < 999, "Число должно быть больше 0 и меньше 1000"

c, rem_C = divmod(decimal, 100)
x, i = divmod(rem_C, 10)
latin = ''

# print(c)
if c == 9:
    latin = latin + "CM"
elif c >= 5:
    latin = latin + "D" + (c - 5) * "C"
elif c == 4:
    latin = latin + "CD"
else:
    latin = latin + c * "C"
# print(x)
if x == 9:
    latin = latin + "XC"
elif x >= 5:
    latin = latin + "L" + (x - 5) * "X"
elif x == 4:
    latin = latin + "XL"
else:
    latin = latin + x * "X"
# print(i)
if i == 9:
    latin = latin + "IX"
elif i >= 5:
    latin = latin + "V" + (i - 5) * "I"
elif i == 4:
    latin = latin + "IV"
else:
    latin = latin + i * "I"

# output
print(latin)
