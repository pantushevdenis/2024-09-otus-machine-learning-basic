# Написать упрощенную версию алгоритма RLE. Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
# Пример:
# aaabbbbccccc -> 3a4b5c
# asssdddsssddd -> 1a3s3d3s3d
# abcba -> 1a1b1c1b1a

data = "aaabbbbccccc"

encoding = []
prev_char = data[0]
count = 1
for char in data[1:]:
    if char == prev_char:
        count += 1
    else:
        encoding.append(str(count) + prev_char)
        prev_char = char
        count = 1

print(encoding)
print("".join(encoding))
