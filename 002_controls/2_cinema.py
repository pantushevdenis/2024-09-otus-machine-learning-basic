# Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0,
# Количество вложенных списков - количество рядов. Пользователь вводит сколько билетов ему требуется.
# Программа должна найти ряд, где можно приобрести нужно количество билетов (места должны быть рядом).
# Если таких рядов несколько, то ближайший к экрану (ближайшим считается нулевой ряд). Ели таких мест нет, то вывести False
# Пример:
# [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]], 2 -> 1
# [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]], 2 -> False


data = [[0, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0]]

# data = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]]


try:
    ticket_nums = int(input("Введите количество билетов: "))
    assert 0 <= ticket_nums
except:
    print("Исходными данными должно быть положительное число")

num_rows = len(data)
finded = False
# print("num_rows =", num_rows)
for i, row in enumerate(data):
    # print("row:", i, row)
    row_size = len(row)
    if row_size >= ticket_nums:
        for subrow in [row[j: j + ticket_nums] for j in range(row_size - ticket_nums + 1)]:
            # print("subrow:", subrow)
            for e in subrow:
                if e == 1:
                    break
            else:
                finded = True
            if finded:
                break
        if finded:
            print(i)
            break
if not finded:
    print(False)


