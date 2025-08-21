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


def inverse(matrix):
    from copy import deepcopy
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            print("Matrix must be square for inversion.")
            return None

    mat = deepcopy(matrix)
    identity = [[float(i == j) for i in range(n)] for j in range(n)]

    for i in range(n):
        if mat[i][i] == 0:
            for j in range(i + 1, n):
                if mat[j][i] != 0:
                    mat[i], mat[j] = mat[j], mat[i]
                    identity[i], identity[j] = identity[j], identity[i]
                    break
            else:
                print("Matrix is singular, can't invert.")
                return None

        pivot = mat[i][i]
        for j in range(n):
            mat[i][j] /= pivot
            identity[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = mat[k][i]
                for j in range(n):
                    mat[k][j] -= factor * mat[i][j]
                    identity[k][j] -= factor * identity[i][j]

    return identity


# --------- Run the inverse tester ---------
print("Enter a square matrix to find its inverse:")
A = read_matrix()

inv = inverse(A)

if inv:
    print("\nInverse of the matrix:")
    for row in inv:
        print(row)
