from matplotlib import pyplot as plt
from collections import Counter

from numpy import histogram

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
print (histogram)
xdata = [x + 5 for x in histogram.keys()]
print("xdata:", xdata)
ydata = histogram.values()
print("ydata:", ydata)
plt.bar(
    xdata,
    ydata,
    width=10,
    edgecolor=(0, 0, 0)
    )
plt.axis((-5, 105, 0, 5))
plt.xticks([i * 10 for i in range(11)])
plt.xlabel("Дециль")
plt.ylabel("Число студентов")
plt.title("Распределение оценок за экзамен № 1")
plt.show()

