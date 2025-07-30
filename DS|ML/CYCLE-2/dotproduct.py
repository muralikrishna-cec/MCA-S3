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


def dot_product(A, B):
    result = []
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Matrix dimensions do not match for dot product.")
        return None

    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            sum_product = 0
            for k in range(cols_A):
                sum_product += A[i][k] * B[k][j]
            row.append(sum_product)
        result.append(row)
    return result


# ---------- Run the code ----------
print("Matrix A:")
A = read_matrix()

print("\nMatrix B:")
B = read_matrix()

print("\nDot Product (A x B):")
D = dot_product(A, B)

if D:
    for row in D:
        print(row)
