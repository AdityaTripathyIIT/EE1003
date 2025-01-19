import numpy as np
import matplotlib.pyplot as plt

def cdf(x):
    if x < 0:
        return 0
    elif 0 <= x < 1:
        return 0.25
    elif 1 <= x < 2:
        return 0.75
    else:
        return 1
x_values = np.linspace(-1, 3, 400)
y_values = np.array([piecewise_function(x) for x in x_values])
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Cumulative Distribution Function', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.savefig("../figs/fig2.png")
