import numpy as np

row = int(input("Enter the rows of matrix: "))
col = int(input("Enter the columns of matrix: "))

matrix = []
for i in range(row):
    rows = []
    for j in range(col):
        elem = int(input(f"Enter element at ({i+1},{j+1}): "))
        rows.append(elem)
    matrix.append(rows)

op = np.array(matrix)
print("Matrix is:")
print(op)
