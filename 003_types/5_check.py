# Пользователь вводит данные, проверить - являются ли они положительным вещественным числом. Не использовать встроенные функции для проверки, только методы данных и конструкцию IF. (Дополнительное задание, по желанию - проверка на отрицательные вещественные числа)
# Пример:
# 5.6 -> True
# .78 -> True
# .67. -> False
# 5 -> True

# data = float(input("Введите данные: "))
# при вводе любого значения возвращает str

# data = 5.6
# data = 0.78
# data = ".67."
data = 5  # будет int, но согласно кейсам должно возвращать true

if (type(data) is float) or (type(data) is int) and data > 0:
    print(True)
else:
    print(False)