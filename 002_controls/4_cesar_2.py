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

ords = (ord(ch) for ch in str_data)
encs_ords = ((a + k - 33) % 94 + 33 if 33 <= a <= 126 else a for a in ords)
encs = (chr(o) for o in encs_ords)
res_str = "".join(encs)

print(res_str)


