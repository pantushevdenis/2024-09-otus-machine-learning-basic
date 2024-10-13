# Написать функцию проверяющую валидность введенной даты.
# Пример:
# 29.02.2000 -> True
# 29.02.2001 -> False
# 31.04.1962 -> False

from datetime import datetime


def validate_str_for_date(str):
    try:
        _ = datetime.strptime(str, "%d.%m.%Y")
        return True
    except:
        return False


assert validate_str_for_date("29.02.2000") == True
assert validate_str_for_date("29.02.2001") == False
assert validate_str_for_date("31.04.1962") == False
