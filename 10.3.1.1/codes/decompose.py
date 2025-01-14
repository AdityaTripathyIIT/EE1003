import numpy as np
from scipy.linalg import lu, solve

A = np.array([[1, -7], [1, -3]], dtype=float)
b = np.array([-42, 6], dtype=float)
P, L, U = lu(A)
y = solve(L, np.dot(P, b))
x = solve(U, y)
print("Solution vector x:", x)

