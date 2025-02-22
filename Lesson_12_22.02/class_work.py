def Floyd_Warshall(adj_matrix):
    n = len(adj_matrix)
    res = [[[0 for i in range(n)] for j in range(n)] for k in range(n + 1)]
    res[0] = adj_matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                res[k + 1][i][j] = min(res[k][i][j], res[k][i][k] + res[k][k][j])
    return res[-1]


m = [
    [0, 2, float('inf'), 2],
    [2, 0, 1, float("inf")],
    [float("inf"), 1, 0, 8],
    [2, float("inf"), 8, 0]
]


M = Floyd_Warshall(m)
for line in M:
    print(*line)


