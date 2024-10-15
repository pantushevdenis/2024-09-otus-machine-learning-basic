# Пользователь в бесконечном цикле вводит данные пользователей:
# имя, затем фамилию, возраст и ID.
# Ввод продолжается до тех пор, пока не будет введено пустое поле.
# Пользователи заносятся в словарь, где ключ это ID пользователя, а остальные данные записываются в виде кортежа.
# Так же программа должна проверять, что имя и фамилия состоят только из символов и начинаются с большой буквы,
# если не с большой, то заменяет на большую, возраст должен быть числом от 18 до 60,
# ID - целое число, дополненное до 8 знаков незначащими нолями, ID должен быть уникальным
# Дополнительно написать функцию, которая будет выводить полученный словарь в виде таблицы
from dis import show_code
from subprocess import check_call
from tabnanny import check

list = {}

def check_and_capitalize_name(str_value):
    """
    Проверяет строку на соответсвие Фамилия или Имя.
    Не допускается пустая строка или одни пробелы.
    Первый символ делается большой
    :param str_value: Имя/Фамилия
    :return: Проверенная и исправленная строка
    """
    str_value = str_value.strip()
    if str_value == "":
        raise ValueError("Имя/Фамилия должно содержать символы")
    if not all(x.isalpha() or x.isspace() for x in str_value):
        raise ValueError("Имя/Фамилия должно содержать только символы и пробелы")
    return str_value.capitalize()

def check_age(str_value):
    """
    Преобразует строку в целое число, возраст.
    Допускается только целые числа больше или равно 18 и меньше 60
    :return: целое число с возрастом
    """
    try:
        age = int(str_value)
        assert 18 <= age <= 60
    except:
        raise ValueError("Строка с возрастом должна быть целым числом больше или равно 18 и меньше или равно 60")
    return age

def check_and_fill_id(str_value):
    try:
        id = int(str_value)
        assert 0 < id <= 99999999
        id_str = str(id)
        id_str_filled = id_str.zfill(8)
        return id_str_filled
    except:
        raise ValueError("Строка ID должна быть целым положительным числов 8 знаков")

def input_data(map_users):
    while True:
        str_value = input("Введите Имя, Фамилию, возраст (от 18 до 60) и ID (через запятую). Для выхода - пробел. :")
        if str_value == " ":
            break
        try:
            name, surname, age_str, id_str = str_value.split(",")
            name = check_and_capitalize_name(name)
            surname = check_and_capitalize_name(surname)
            age = check_age(age_str)
            id = check_and_fill_id(id_str)

            map_users[id] = (name, surname, age)
        except:
            print("Необходимо ввести четыре значения - имя и фамилию как строки, возраст как положительное число от 18 до 60")
            continue




def show_data(map_users: dict):
    max_len_name = 4
    max_len_surname = 7
    for id_value, (name, surname, age) in map_users.items():
        max_len_name = len(name) if len(name) > max_len_name else max_len_name
        max_len_surname = len(surname) if len(surname) > max_len_surname else max_len_surname
    fmt = "{}|{:{align}{max_len_name_p}}|{:{align}{max_len_surname_p}}|{:>3}|"
    print(fmt.format("id      ", "name", "surname", "age", align="<", max_len_name_p=max_len_name, max_len_surname_p=max_len_surname))
    for id_value, (name, surname, age) in map_users.items():
       print(fmt.format(id_value, name, surname, age, align="<", max_len_name_p=max_len_name, max_len_surname_p=max_len_surname))

####
map_users = {}
input_data(map_users)
show_data(map_users)
exit(0)


mp = {"00000001": ("Den", "Pan", 20)}
show_data(mp)

assert check_and_capitalize_name("Пантюшев") == "Пантюшев"
assert check_and_capitalize_name("пантюшев") == "Пантюшев"
try:
    assert check_and_capitalize_name("") == ""
except:
    print("check_name(\"\") is except")

try:
    assert check_and_capitalize_name(" ") == ""
except:
    print("check_name(\"\") is except")

assert check_age("20") == 20

try:
    check_age("")
except:
    print("check_age(\"\") is except")

try:
    check_age("10")
except:
    print("check_age(\"10\") is except")

try:
    check_age("61")
except:
    print("check_age(\"61\") is except")


