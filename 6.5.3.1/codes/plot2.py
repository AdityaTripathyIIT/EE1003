import cvxpy as cp
import numpy as np

# Define the known vector O
O = np.array([0, 0])  # Replace O1 and O2 with the actual values

# Define the optimization variable x
x = cp.Variable(2)

# Define the objective function (x - O)^T(x - O)
objective = cp.Minimize(cp.sum_squares(x - O))

# Define the constraint x^Te_2 = 1
e_2 = np.array([0, 1])
constraint = [x @ e_2 == 1]

# Define the problem and solve it
problem = cp.Problem(objective, constraint)
problem.solve()

# Print the results
print("Optimal value of x:", x.value)
print("Optimal objective value:", problem.value)

