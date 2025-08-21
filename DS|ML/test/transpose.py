def read_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    print("Enter matrix row by row (space separated):")
    for i in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print("Invalid number of columns.")
            return None
        matrix.append(row)
    return matrix


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed


# -------- Run Transpose Tester --------
print("Enter a matrix to transpose:")
A = read_matrix()

if A:
    T = transpose(A)
    print("\nTransposed matrix:")
    for row in T:
        print(row)
