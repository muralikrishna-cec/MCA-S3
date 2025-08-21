import numpy as np

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

dot_product = np.dot(A, B)
print("Dot product:\n", dot_product)
