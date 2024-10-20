import math

def amulet_perimetr(a, b, c):
    return (a + b + c) / 2


def amulet_area(a, b, c):
    p = amulet_perimetr(a, b, c)
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


assert amulet_area(3, 4, 5) == 6