import numpy as np

A = np.array([[150, 300, 50], [5, 15, 1], [25, 0, 0], [0, 30, 0]], dtype=float)
b = np.array([1000, 50, 125, 60], dtype=float)

A_T = A.T
A_T_A = np.dot(A_T, A)
A_T_b = np.dot(A_T, b)
A_T_A_inv = np.linalg.inv(A_T_A)
x = np.dot(A_T_A_inv, A_T_b)

error = np.linalg.norm(np.dot(A, x) - b)
print(x)
print(error)