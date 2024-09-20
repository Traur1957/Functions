def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        k = []
        for j in range(m):
            k.append(value)
        matrix.append(k)
    return matrix

print(get_matrix(n = 2, m = 2, value = 10))