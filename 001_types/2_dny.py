# Отпуск. Пользователь вводит сколько дней осталось до ближайшего отпуска.
# Программа должна вывести количество выходных дней до отпуска, если учесть,
# что выходные это суббота и воскресенье, сегодня понедельник и праздники мы не учитываем.
# Пример:
# 4 -> 0
# 6 -> 1
# 14 -> 4

days_number_to_vacation = 16

assert days_number_to_vacation >= 0

NUMBER_WORK_DAYS_IN_WEEK = 5

number_full_weeks, remainder = divmod(days_number_to_vacation, 7)
# print(f"{number_full_weeks} {remainder}")
number_day_off_of_remainder = remainder - NUMBER_WORK_DAYS_IN_WEEK
number_days_off = number_full_weeks * 2 + 0 if number_day_off_of_remainder < 0 else number_day_off_of_remainder
number_working_days = number_full_weeks * 5 + remainder

print(number_days_off)





