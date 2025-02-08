def read_edge_list():
    N = int(input())
    M = int(input())
    res = []
    for i in range(M):
        x, y = (int(x) for x in input().split())
        res.append((x, y))
    return N, res


def adj_matrix(N, edge_list):
    res = [[0 for j in range(N)] for i in range(N)]

    for x, y in edge_list:
        res[x][y] = 1
        res[y][x] = 1

    return res

def adj_list(N, edge_list):
    res = [[] for i in range(N)]

    for x, y in edge_list:
        res[x].append(y)
        res[y].append(x)

    return res


def print_matrix(A):
    for line in A:
        print(*line)


def DFS(curr_node, adj_list, visited=None):
    if visited is None:
        visited = set()
    visited.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node not in visited:
            DFS(adj_node, adj_list, visited)
    return visited


N, edges = read_edge_list()
graph = adj_list(N, edges)
all_visited = set()
components = []

for node in range(N):
    if node not in all_visited:
        comp = DFS(node, graph)
        all_visited |= comp
        components.append(comp)
print(components)

