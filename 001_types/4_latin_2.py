# num = 643
from builtins import print

try:
    num = int(input("Введите число больше 0 и меньше 2000: "))
    assert 0 < num < 2000
except:
    print("Число должно быть больше 0 и меньше 2000")
    exit()

all_roman = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')]

roman = ''
while num > 0:
    for i, r in all_roman:
        while num >= i:
            roman += r
            num -= i

print(roman)
