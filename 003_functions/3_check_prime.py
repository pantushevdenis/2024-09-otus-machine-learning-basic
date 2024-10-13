# Функция проверки на простое число. Простые числа – это такие числа, которые делятся на себя и на единицу.
# Пример:
# 17 -> True
# 20 -> False
# 23 -> True
from distutils.command.check import check

from math import sqrt

def check_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    if n > 1:
        return True


assert check_prime(17) == True
assert check_prime(20) == False
assert check_prime(23) == True



