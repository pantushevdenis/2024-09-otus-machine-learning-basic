from matplotlib import pyplot as plt

movies = ["Энни Холл", "Бег Гур", "Касабланка",  "Ганди", "Вестсайдская история"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)
plt.title("Мои любимые фильмы")
plt.ylabel("Количество наград")
plt.xticks(range(len(movies)), movies)

plt.show()