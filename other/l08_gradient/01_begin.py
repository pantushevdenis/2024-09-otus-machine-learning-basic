import random

from other.l04_linear_algebra.my_linear_algebra import Vector
import other.l04_linear_algebra.my_linear_algebra as mla
import other.l08_gradient.my_gradients as mg

def sum_of_squares(v: Vector) -> float:
    return mla.vector_dot(v, v)

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]


v = [random.uniform(-10, 10) for i in range(3)]
print(v)

for epoch in range(1000):
    grad = sum_of_squares_gradient(v)
    v = mg.gradient_step(v, grad, -0.01)
    print(epoch, v)

