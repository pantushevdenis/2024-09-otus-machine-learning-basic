import statistics as st
import my_statistics as mst

from typing import List

from other.l05_statistics.my_statistics import my_range

num_friends = [100, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10,
               10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
               9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
               3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1]

num_points = len(num_friends)
print(f"numpoints: {num_points}")

smallest_value = min(num_friends)
print(f"smallest value: {smallest_value}")

largest_value = max(num_friends)
print(f"largest value: {largest_value}")

num_friends_sorted = sorted(num_friends)
print(f"sorted values: {num_friends_sorted}")

print(f"smallest values: {num_friends_sorted[0]}, {num_friends_sorted[1]}, {num_friends_sorted[2]}")
print(f"largets values: {num_friends_sorted[-1]}, {num_friends_sorted[-2]}, {num_friends_sorted[-3]}")

print(f"first 10: {num_friends_sorted[:10]}")
print(f"last 10: {num_friends_sorted[-10:]}")


def my_mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


print(f"my_mean: {my_mean(num_friends)}")
print(f"my_mean without last: {my_mean(num_friends_sorted[:-1])}")
print(f"st.mean: {st.mean(num_friends)}")
print(f"st.median: {st.median(num_friends)}")
print(f"st.median without last: {st.median(num_friends_sorted[:-1])}")
print(f"st.quantile 10: {st.quantiles(num_friends, n=10)}")
print(f"st.mode: {st.mode(num_friends)}")

print(f"my_range: {my_range(num_friends)}")

print(f"my_variance: {mst.my_variance(num_friends)}")
print(f"variance: {st.variance(num_friends)}")

print(f"my_standard_deviation: {mst.my_standard_deviation(num_friends)}")
print(f"standard_deviation: {st.stdev(num_friends)}")
print(f"standard_deviation without last: {st.stdev(num_friends_sorted[:-1])}")  # влияние выброса


