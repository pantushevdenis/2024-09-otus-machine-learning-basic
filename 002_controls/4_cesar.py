# Шифр Цезаря. Пользователь вводит строку и ключ шифра, программа должна вывести зашифрованную строку (со сдвигом по ключу). Сдвиг циклический.
# Используем только латинский алфавит, пробелы не шифруются.
# Пример:
# Dog, 2 -> Fqi
# Zak zak, 3 -> Cdn cdn
# Python is the BEST, 5 -> Udymts nx ymj GJXY

str_data = input("Введите строку: ")
try:
    k = int(input("Введите ключ: "))
    assert k > 0
except:
    print("Ключ должен быть целым положительным числом")
    exit()

res_arr = []
for ch in str_data:
    a = ord(ch)
    res = (a + k - 33) % 94 + 33 if 33 <= a <= 126 else a
    res_arr.append(chr(res))
res_str = "".join(res_arr)

print(res_str)


