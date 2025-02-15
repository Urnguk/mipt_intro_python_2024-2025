def acyclic(curr_node, adj_list, grey=None, black=None, prev_node=None):
    if grey is None:
        grey = set()
    if black is None:
        black = set()

    if curr_node in grey:
        return False
    if curr_node in black:
        return True

    grey.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node != prev_node and acyclic(adj_node, adj_list, grey, black, curr_node):
            return False

    grey.discard(curr_node)
    black.add(curr_node)
    return True


def DFS(curr_node, adj_list, visited=None):
    if visited is None:
        visited = set()
    visited.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node not in visited:
            DFS(adj_node, adj_list, visited)
    return visited


def BFS(start_node, adj_list, visited=None):
    queue = [(start_node, 0)]
    if visited is None:
        visited = set()
    while len(queue) > 0:
        curr_node, dist = queue.pop(0)
        visited.add(curr_node)
        for adj_node in adj_list[curr_node]:
            if adj_node not in visited:
                queue.append((adj_node, dist + 1))
    return visited


def min_dist(start_node, finish_node, adj_list, visited=None):
    queue = [(start_node, 0)]
    if visited is None:
        visited = set()
    while len(queue) > 0:
        curr_node, dist = queue.pop(0)
        if curr_node == finish_node:
            return dist
        visited.add(curr_node)
        for adj_node in adj_list[curr_node]:
            if adj_node not in visited:
                queue.append((adj_node, dist + 1))
    return float("inf")


def dijkstra(start_node, adj_list):
    dist = {i: float("inf") for i in range(len(adj_list))}
    dist[start_node] = 0
    res = {}
    while dist:
        j = 0
        min_d = min(dist.values())
        for i in dist:
            if dist[i] == min_d:
                j = i

        for adj_node, edge_weight in adj_list[j]:
            dist[adj_node] = min(dist[adj_node], dist[j] + edge_weight)

        res[j] = dist[j]
        dist.pop(j)
    return res



























