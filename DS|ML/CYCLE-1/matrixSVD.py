import numpy as np

A = np.array([[1,2],
              [3,4]])

print("Matrix A:\n", A)

U, S, Vt = np.linalg.svd(A)
print("U matrix:\n", U)
print("Singular values:\n", S)
print("V transpose:\n", Vt)
