import random

from other.l04_linear_algebra.my_linear_algebra import Vector, vector_dot, scalar_multiply, add

def sum_of_squares(v: Vector) -> float:
    return vector_dot(v, v)

def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]

def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    assert len(v)== len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)


v = [random.uniform(-10, 10) for i in range(3)]
print(v)

for epoch in range(1000):
    grad = sum_of_squares_gradient(v)
    v = gradient_step(v, grad, -0.01)
    print(epoch, v)

