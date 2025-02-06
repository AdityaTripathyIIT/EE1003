import numpy as np
import matplotlib.pyplot as plt
import ctypes
from scipy.stats import binom, norm
gen = ctypes.CDLL('./sim.so')
gen.theoretical_binomial.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
gen.theoretical_binomial.restype = None
gen.sim_binomial.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
gen.sim_binomial.restype = None

fig, ax = plt.subplots(2,2,figsize=(8, 6))
n = 20
p = 0.5
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(0, n, 1000)
y = norm.pdf(x, mu, sigma)
ax[0,0].plot(x, y, 'r-')
x_values = np.array([x for x in range(n + 1)])
y_values = np.zeros((1, n+1), dtype = np.double)
gen.sim_binomial(
        n, p, y_values.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        )
markerline, stemlines, baseline = ax[0,0].stem(x_values, y_values[0], label = "n=20")
plt.setp(markerline, 'markerfacecolor', 'red')
plt.setp(stemlines, 'color', 'red')
plt.setp(baseline, 'color', 'gray', 'linewidth', 1)
ax[0,0].legend(loc = "best")
n = 50
p = 0.5
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(0, n, 1000)
y = norm.pdf(x, mu, sigma)
ax[0,1].plot(x, y, 'g-')
x_values = np.array([x for x in range(n + 1)])
y_values = np.zeros((1, n+1), dtype = np.double)
gen.sim_binomial(
        n, p, y_values.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        )
markerline, stemlines, baseline = ax[0,1].stem(x_values, y_values[0], label = "n=50")
plt.setp(markerline, 'markerfacecolor', 'green')
plt.setp(stemlines, 'color', 'green')
plt.setp(baseline, 'color', 'gray', 'linewidth', 1)
ax[0,1].set_xlim(10,40)
ax[0,1].legend(loc = "best")
n = 100
p = 0.5
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(0, n, 1000)
y = norm.pdf(x, mu, sigma)
ax[1,0].plot(x, y, 'b-')
x_values = np.array([x for x in range(n + 1)])
y_values = np.zeros((1, n+1), dtype = np.double)
gen.sim_binomial(
        n, p, y_values.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        )
markerline, stemlines, baseline = ax[1,0].stem(x_values, y_values[0], label = "n=100")
plt.setp(markerline, 'markerfacecolor', 'blue')
plt.setp(stemlines, 'color', 'blue')
plt.setp(baseline, 'color', 'gray', 'linewidth', 1)

ax[1,0].set_xlim(20,80)
ax[1,0].legend(loc = "best")
n = 200
p = 0.5
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(0, n, 1000)
y = norm.pdf(x, mu, sigma)
ax[1,1].plot(x, y, 'orange')
x_values = np.array([x for x in range(n + 1)])
y_values = np.zeros((1, n+1), dtype = np.double)
gen.sim_binomial(
        n, p, y_values.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        )
markerline, stemlines, baseline = ax[1,1].stem(x_values, y_values[0], label = "n=200")
plt.setp(markerline, 'markerfacecolor', 'orange')
plt.setp(stemlines, 'color', 'orange')
plt.setp(baseline, 'color', 'gray', 'linewidth', 1)
ax[1,1].set_xlim(70, 130)
ax[1,1].legend(loc = "best")
plt.tight_layout()
plt.savefig("../figs/binomial_sub.png")
plt.show()

