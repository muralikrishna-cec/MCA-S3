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


def rank(matrix):
    from copy import deepcopy
    mat = deepcopy(matrix)
    rows = len(mat)
    cols = len(mat[0])
    rank = 0

    for r in range(rows):
        if rank >= cols:
            break
        if abs(mat[r][rank]) < 1e-10:
            for i in range(r + 1, rows):
                if abs(mat[i][rank]) > 1e-10:
                    mat[r], mat[i] = mat[i], mat[r]
                    break
            else:
                rank += 1
                continue

        pivot = mat[r][rank]
        for j in range(cols):
            mat[r][j] /= pivot

        for i in range(rows):
            if i != r:
                factor = mat[i][rank]
                for j in range(cols):
                    mat[i][j] -= factor * mat[r][j]

        rank += 1

    # Count non-zero rows
    non_zero_rows = 0
    for row in mat:
        if any(abs(x) > 1e-10 for x in row):
            non_zero_rows += 1

    return non_zero_rows


# ---------- Test the rank function ----------
print("Enter matrix to find its rank:")
A = read_matrix()

r = rank(A)
print(f"\nRank of the matrix: {r}")

 
