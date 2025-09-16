import numpy as np

A = np.array([[1,2],
              [3,4]])

print("Matrix A:\n", A)

rank_A = np.linalg.matrix_rank(A)
print("Rank of Matrix:", rank_A)
