import numpy as np

row = int(input("Enter rows: "))
col = int(input("Enter cols: "))

matrix = []
for i in range(row):
    rows = []
    for j in range(col):
        elem = int(input("Enter element: "))
        rows.append(elem)
    matrix.append(rows)

op = np.array(matrix)
op1 = op.T

print("Original Matrix:\n", op)
print("Transpose Matrix:\n", op1)
