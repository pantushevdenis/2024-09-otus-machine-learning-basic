# Пользователь вводит длину и ширину плитки шоколада, а также размер куска, который хочет отломить, программа должна вычислить - можно ли совершить подобный разлом или нет, если учесть, что ломать можно только по прямой
# Пример:
# 3, 4, 6 -> True
# 5, 7, 8 -> False
# 4, 5, 12 -> True

# L, H, a

input_str = input("Введите длину и ширину плитки шоколада, а также размер куска: ")
try:
    l_str, h_str, a_str = input_str.split(",")
    l = int(l_str)
    h = int(h_str)
    a = int(a_str)
    assert 0 < l
    assert 0 < h
    assert 0 < a
except:
    print("Длина, ширина и размер куска должны быть целыми числами большее нуля")
    exit()

b1, b_rem1 = divmod(a, l)
b2, b_rem2 = divmod(a, h)

if (b1 > 0 and b_rem1 == 0) or (b2 > 0 and b_rem2 == 0):
    print(True)
else:
    print(False)
