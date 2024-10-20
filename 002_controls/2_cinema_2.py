import itertools as it

data = [[0, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0]]

# data = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]]

try:
    ticket_nums = int(input("Введите количество билетов: "))
    assert 0 <= ticket_nums
except:
    print("Исходными данными должно быть положительное число")

for i, row in enumerate(data):
    # print("row:", i, row)
    subrows = ((n, sum(1 for _ in gr)) for n, gr in it.groupby(row))
    subrows_filtered = ((n, c) for n, c in subrows
               if n == 0 and c >= ticket_nums)
    for e in subrows_filtered:
        print(i)
        exit()
print(False)



