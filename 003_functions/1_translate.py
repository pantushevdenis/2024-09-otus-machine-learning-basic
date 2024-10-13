# Написать функцию, которая будет перводит снейк_кейс в КэмелКейс и наоборот. Функция сама определяет - какой формат ей передали. Можно добавить ключевой аргумент, который будет принудительно возвращать один из форматов.
# Пример:
# otus_course -> OtusCourse
# PythonIsTheBest -> python_is_the_best


def translate(str):
    if ("_" in str):
        return "".join(x.capitalize() for x in str.split("_"))
    else:
        return ''.join(("_" if i > 0 else "") + e.lower() if e.isupper() else e for i, e in enumerate(str))


assert translate("otus_course") == "OtusCourse"
assert translate("PythonIsTheBest") == "python_is_the_best"