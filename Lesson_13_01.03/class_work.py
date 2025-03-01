def bipartite(adj_list, start_node):
    nodes = [None for i in range(len(adj_list))]
    queue = [(start_node, 0)]
    while queue:
        curr_node, curr_state = queue.pop(0)
        nodes[curr_node] = curr_state
        for adj_node in adj_list[curr_node]:
            if nodes[adj_node] is None:
                queue.append((adj_node, int(not(curr_state))))
            elif nodes[adj_node] == curr_state:
                return False
    return True


# A = [
#     [2, 3, 1],
#     [3, 6, 2],
#     [0, 4, 8]
# ]
#
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         A[i][j], A[j][i] = A[j][i], A[i][j]
#
# for line in A:
#     print(*line)

# def DFS(curr_node, adj_matrix, reverse=False, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(curr_node)
#     for adj_node in range(len(adj_matrix)):
#         if ((reverse and adj_matrix[adj_node][curr_node] == 1 or
#               (not reverse) and adj_matrix[curr_node][adj_node] == 1)):
#             if adj_node not in visited:
#                 DFS(adj_node, adj_matrix, reverse, visited)
#     return visited
#
#
# def connect_comp(start_node, adj_matrix):
#     fd_set = DFS(start_node, adj_matrix)
#     bd_set = DFS(start_node, adj_matrix, reverse=True)
#     return fd_set & bd_set


def DFS(curr_node, adj_list, stack=None, visited=None):
    if visited is None:
        visited = set()
    if stack is None:
        stack = []
    visited.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node not in visited:
            DFS(adj_node, adj_list, stack, visited)
    stack.append(curr_node)
    return stack




