# Отпуск. Пользователь вводит сколько дней осталось до ближайшего отпуска. Программа должна вывести количество выходных дней до отпуска, если учесть? что выходные это суббота и воскресенье, сегодня понедельник и праздники мы не учитываем.
# Пример:
# 4 -> 0
# 6 -> 1
# 14 -> 4

days_number_to_vacation = 4

assert days_number_to_vacation >= 0

number_sull_weeks, remainder = divmod(days_number_to_vacation, 7)

print(number_sull_weeks, remainder)




