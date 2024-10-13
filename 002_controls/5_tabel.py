# Табель успеваемости. Пользователь в бесконечном цикле (пока не будет введена пустая строка) вводит строки вида:
# 'название предмета' 'фамилия ученика' 'оценка'.
# После окончания ввода программа выводит в консоль Название предмета, далее список учеников и все их оценки в виде таблицы
#
# Математика Иванов 5
# Математика Иванов 4
# Литература Иванов 3
# Математика Петров 5
# Литература Сидоров 3
# Литература Петров 5
# Литература Иванов 4
# Математика Сидоров 3
# Математика Петров 5
#
# Математика
# Иванов 5 4
# Петров 5 5
# Сидоров 3
#
# Литература
# Ивванов 3 4
# Сидоров 3
# Петров 5


list = []

while True:
    str = input("Введите предмет, фамилию, оценку. Для выхода - пробел. :")
    if str == " ":
        break
    try:
        lesson, surname, grade_str = str.split()
        grade = int(grade_str)
        assert 1 <= grade <= 5
    except:
        print("Необходимо ввести три значения - предмет и фамилию как строки и оценку как положительное число от 1 до 5")
        continue

    print(lesson, surname, grade)
    list.append((lesson, surname, grade))

# list.append(("Математика", "иванов", 3))
# list.append(("Математика", "иванов", 4))
# list.append(("Математика", "иванов", 4))
# list.append(("Литература", "иванов", 4))
# list.append(("Литература", "иванов", 5))
# list.append(("Литература", "Петров", 5))
# list.append(("Литература", "Петров", 6))

grades_for_studens  = {}
for l, s, g in list:
    if l not in grades_for_studens:
        grades_for_studens[l] = {}
    if s not in grades_for_studens[l]:
        grades_for_studens[l][s] = []
    grades_for_studens[l][s].append(g)

print()
for l_key in grades_for_studens:
    print(l_key)
    for s_key in grades_for_studens[l_key]:
        print(s, " ".join(str(d) for d in grades_for_studens[l_key][s_key]))
    print()

