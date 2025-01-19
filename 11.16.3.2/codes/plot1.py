import numpy as np
import matplotlib.pyplot as plt

def pmf(x):
    if x == 0:
        return 0.25
    elif x == 1:
        return 0.5
    elif x == 2:
        return 0.25
    else:
        return 0

x_values = np.array([-0.5, 0, 0.5, 1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
y_values = np.array([pmf(x) for x in x_values])

# Create the stem plot
plt.figure(figsize=(8, 6))
markerline, stemlines, baseline = plt.stem(x_values, y_values)
plt.setp(markerline, 'markerfacecolor', 'red')
plt.setp(stemlines, 'color', 'red')
plt.setp(baseline, 'color', 'gray', 'linewidth', 1)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.savefig("../figs/fig1.png")

