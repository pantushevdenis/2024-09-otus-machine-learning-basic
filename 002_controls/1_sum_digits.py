# Пользователь вводит целое число, программа складывает все цифры числа, с полученным числом - то же самое и так до тех пор, пока не получится однозначное число.
# Пример:
# 545 -> 5
# 12345 -> 6

try:
    num = int(input("Введите любое большое число: "))
    assert 0 <= num
except:
    print("Исходными данными должно быть положительное число")

while True:
    sum_digit = 0
    while num > 0:
        num, digit = divmod(num, 10)
        sum_digit = sum_digit + digit
    # print(sum_digit)
    if sum_digit < 10:
        break
    num = sum_digit

print(sum_digit)
