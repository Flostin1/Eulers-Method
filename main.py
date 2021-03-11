import math
import numpy as np
import matplotlib.pyplot as plt

def f(n):
    return math.e**-n**2

# b MUST be greater than a
a = -5
b = 5
dx = 0.001

x = np.arange(a, b, dx)
y = np.array([f(i) for i in x])
plt.plot(x, y)

# Euler's Method
def euler_method():
    initial_condition = 0
    slope = 0
    y_values = []

    # Applies euler's method starting from 0 and stopping at 'b'
    for x_i in np.arange(0, b, dx):
        slope = f(x_i)
        initial_condition += slope * dx
        y_values.append(initial_condition)

    # Applies euler's method starting from 0 and stopping at 'a'
    initial_condition = 0
    for x_i in np.arange(0, a, -dx):
        slope = f(x_i)
        initial_condition -= slope * dx
        y_values.insert(0, initial_condition)
    
    return y_values

y_2 = np.array(euler_method())
plt.plot(x, y_2)

plt.show()