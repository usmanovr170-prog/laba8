n = 3
m = 4

matrix = [
    [1, -2, 3, 4],
    [5, 6, -7, 8],
    [-9, 10, 11, -12]
]

for i in range(n):
    for j in range(m):
        if matrix[i][j] < 0:
            matrix[i][j] = 0

for row in matrix:
    print(row)