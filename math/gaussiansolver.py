import numpy as np

A = np.array([[150, 300, 50], [5, 15, 1], [25, 0, 0]], dtype=float)
b = np.array([1000, 50, 125], dtype=float)

n = len(b)
Ab = np.hstack([A, b.reshape(-1, 1)])

for i in range(n):
    pivot = Ab[i][i]
    Ab[i] = Ab[i] / pivot
    for j in range(i + 1, n):
        Ab[j] = Ab[j] - Ab[j][i] * Ab[i]

x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = Ab[i, n] - np.dot(Ab[i, i+1:n], x[i+1:n])

print(x)