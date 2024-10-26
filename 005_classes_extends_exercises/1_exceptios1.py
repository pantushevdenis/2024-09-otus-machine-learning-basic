from builtins import ZeroDivisionError


class MyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Мое исключение: {self.value}"

class MyExceptionZeroDivision(MyException):
    pass

a = 100
b = 0
#b = '0'

try:
    raise MyExceptionZeroDivision(10010)
    raise MyException(100000)
    print(a/b)
    # print(qq) # идет в общее исключение
    print("После ошибочного кода")
except ZeroDivisionError as e:
    print(f"На ноль делить нельзя {e}")
except TypeError:
    print(f'Неверные типы')
except MyExceptionZeroDivision as e:
    print(f"Моя ошибка деление на ноль {e.value}")
except MyException as e:
    print(f"Моя ошибка {e} значение: {e.value}")
#except Exception:
#    print(f"Общее исключение")

finally:
    print("Конец кода")


