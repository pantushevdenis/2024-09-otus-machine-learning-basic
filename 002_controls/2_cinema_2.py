import itertools as it

data = [[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]
# data = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]]

ticket_nums = 2
print("data:", data)
print("ticket nums", ticket_nums)

for i, row in enumerate(data):
    # print("row:", i, row)
    subrows = ((n, sum(1 for _ in gr)) for n, gr in it.groupby(row))
    subrows_filtered = ((n, c) for n, c in subrows
               if n == 0 and c >= ticket_nums)
    for e in subrows_filtered:
        print(i)
        exit()
print(False)



