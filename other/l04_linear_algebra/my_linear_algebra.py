from builtins import super
from typing import List
import math

from numpy import number
from pyparsing import version_info

Vector = List[float]


def add(a: Vector, b: Vector) -> Vector:
    """Сумма соответствующих элементов"""
    assert len(a) == len(b)
    return [ae + be for ae, be in zip(a, b)]


def subtract(a: Vector, b: Vector) -> Vector:
    """Разность соответствующих элементов"""
    assert len(a) == len(b)
    return [ae - be for ae, be in zip(a, b)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Суммирование всех соответствующих элементов"""
    assert vectors, "Векторы не предоставлены"
    num_elements = len(vectors[0])
    assert all(num_elements == len(v) for v in vectors), "Векторы разного размера"
    return [sum(vector[i] for vector in vectors)
           for i in range(num_elements)]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Умножает каждый элемент v на c"""
    return [c * v_i for v_i in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    """Покомпонентые средние"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def vector_dot(a: Vector, b: Vector)-> float:
    """Точечное произведение векторов"""
    assert len(a) == len(b), "Векторы должны иметь одинаковую длину"
    return sum(a_i * b_i for a_i, b_i in zip(a, b))

def vector_sum_of_aquares(v: Vector) -> float:
    """Сумму квадратов элементов вектора"""
    return vector_dot(v, v)

def vector_magnitude(v: Vector) -> float:
    """Магнитуда (длина вектора)"""
    return math.sqrt(vector_sum_of_aquares(v))

def vector_squared_distance(a: Vector, b: Vector) -> float:
    return vector_sum_of_aquares(subtract(a, b))

def vector_distance(a: Vector, b: Vector) -> float:
    return math.sqrt(vector_squared_distance(a, b))





if __name__ == "__main__":
    assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert subtract([5, 7, 9], [1, 2, 3]) == [4, 5, 6]
    assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
    assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
    assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
    assert vector_dot([1, 2, 3], [4, 5, 6]) == 32
    assert vector_sum_of_aquares([1, 2, 3]) == 14
    assert vector_magnitude([3, 4]) == 5
