import numpy as np

A = np.array([[1,2],
              [3,4]])

print("Matrix A:\n", A)

inverse_A = np.linalg.inv(A)
print("Inverse of A:\n", inverse_A)
