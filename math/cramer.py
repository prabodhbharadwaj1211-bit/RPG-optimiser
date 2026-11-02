import numpy as np

A = np.array([[150, 300, 50], [5, 15, 1], [25, 0, 0]], dtype=float)
b = np.array([1000, 50, 125], dtype=float)

n = A.shape[0]
det_A = np.linalg.det(A)
x = np.zeros(n)

for i in range(n):
    A_i = A.copy()
    A_i[:, i] = b
    x[i] = np.linalg.det(A_i) / det_A

print(x)