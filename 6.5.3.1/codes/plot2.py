import cvxpy as cp
import numpy as np

O = np.array([0, 0])  # Replace O1 and O2 with the actual values

x = cp.Variable(2)

objective = cp.Minimize(cp.sum_squares(x - O))

e_2 = np.array([0, 1])
constraint = [x @ e_2 == 1]

problem = cp.Problem(objective, constraint)
problem.solve()

print("Optimal value of x:", x.value)
print("Optimal objective value:", problem.value)

