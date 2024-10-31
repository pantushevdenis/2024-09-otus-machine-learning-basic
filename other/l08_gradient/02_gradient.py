import random

from other.l04_linear_algebra.my_linear_algebra import Vector
import other.l04_linear_algebra.my_linear_algebra as mla
import other.l08_gradient.my_gradients as mg

inputs = [(x, 20 * x + 5) for x in range(-50, 50)]
print(inputs)

def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept
    error = predicted - y
    squared_error = error ** 2
    grad = [2 * error * x, 2 * error]
    return grad

theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
print("theta: ", theta)

learning_rate = 0.001

for epoch in range(5000):
    print("epoch: ", epoch)
    gradients = [linear_gradient(x, y, theta) for x, y in inputs]
    print("gradients: ", gradients)
    grad = mla.vector_mean(gradients)
    print("grad: ", grad)
    theta = mg.gradient_step(theta, grad, -learning_rate)
    print("theta: ", theta)
