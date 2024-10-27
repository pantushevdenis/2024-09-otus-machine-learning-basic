import math
import statistics as st
from typing import List

from other.l04_linear_algebra import my_linear_algebra as la


def my_deviation_of_mean(xs: List[float]) -> List[float]:
    x_bar = st.mean(xs)
    return [x - x_bar for x in xs]


def my_variance(xs: List[float]) -> float:
    assert len(xs) >= 2, "Требуется не менее двух элементов"
    deviation = my_deviation_of_mean(xs)
    return la.vector_sum_of_aquares(deviation) / (len(xs) - 1)

def my_standard_deviation(xs: List[float]) -> float:
    return math.sqrt(my_variance(xs))


def my_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


def my_covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs и xs должы иметь одинаковое число элементв"
    return la.vector_dot(my_deviation_of_mean(xs), my_deviation_of_mean(ys)) / (len(xs) - 1)


def my_correlation(xs: List[float], ys: List[float]) -> float:
    stdev_x = my_standard_deviation(xs)
    stdev_y = my_standard_deviation(ys)

    if stdev_x > 0 and stdev_y > 0:
        return my_covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0