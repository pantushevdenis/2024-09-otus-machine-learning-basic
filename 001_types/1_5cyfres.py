# Пользователь вводит пятизначное число. Программа должна зеркально отразить центральные три цифры. Первая и последняя остаются на местах.
# Пример:
# 23456 -> 25436
# 30789 -> 38709
from hmac import new

try:
    num = int(input("Введите пятизначное целое число: "))
    assert 10000 <= num <= 99999
except:
    print("Число должно быть больше либо равно 10000 и меньше либо равно 99999")
    exit()

# print(type(num))
str_num = str(num)
# print(type(str_num))
central_symbols = str_num[1:4]
reverted_central_symbols = central_symbols[::-1]
new_str_num = str_num[0] + reverted_central_symbols + str_num[4]
new_num = int(new_str_num)

print(new_str_num)
