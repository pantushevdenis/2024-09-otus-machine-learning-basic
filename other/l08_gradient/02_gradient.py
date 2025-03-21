import random
import pandas as pd
import matplotlib.pyplot as plt

from other.l04_linear_algebra.my_linear_algebra import Vector
import other.l04_linear_algebra.my_linear_algebra as mla
import other.l08_gradient.my_gradients as mg

inputs = [(x, 20 * x + 5) for x in range(-50, 50)]
print(inputs)


def calc_predict(x: float, theta: Vector) -> float:
    slope, intercept = theta
    predicted = slope * x + intercept
    return predicted


def calc_error2(p: float, y: float) -> float:
    error = p - y
    return error


def calc_error3(x: float, y: float, theta: Vector) -> float:
    predicted = calc_predict(x, theta)
    error = predicted - y
    return error


def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    predict = calc_predict(x, theta)
    error = calc_error2(predict, y)
    squared_error = error ** 2
    grad = [2 * error * x, 2 * error]
    return grad


theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
print("theta: ", theta)

learning_rate = 0.001

index = []
ds_squared_errors = []

for epoch in range(5000):
    index.append(epoch)
    print("epoch: ", epoch)
    gradients = [linear_gradient(x, y, theta) for x, y in inputs]

    squared_errors = [calc_error3(x, y, theta) ** 2 for x, y in inputs]
    squared_error = sum(squared_errors) / len(squared_errors)
    ds_squared_errors.append(squared_error)

    # print("gradients: ", gradients)
    grad = mla.vector_mean(gradients)
    # print("grad: ", grad)
    theta = mg.gradient_step(theta, grad, -learning_rate)
    print("theta: ", theta, "squared_error: ", squared_error)

# df = pd.DataFrame(ds_squared_errors, columns=['sqerror'], index=index)
# plt.plot(df)
# plt.show()

