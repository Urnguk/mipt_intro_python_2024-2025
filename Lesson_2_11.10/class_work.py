import time
# N = int(input())
# start_time = time.time()
# spells = [float("inf") for i in range(N + 1)]
# spells[1] = 0
# for i in range(1, N):
#     moves = [i + 1]
#     if 2 * i <= N:
#         moves.append(2 * i)
#     if 3 * i <= N:
#         moves.append(3 * i)
#     for j in moves:
#         spells[j] = min(spells[i] + 1, spells[j])
# print(spells[-1])
#
# trace = [N]
# j = N
# while j != 1:
#     if spells[j - 1] + 1 == spells[j]:
#         trace.append(j - 1)
#         j = j - 1
#     elif j % 2 == 0 and spells[j // 2] + 1 == spells[j]:
#         trace.append(j // 2)
#         j = j // 2
#     elif j % 3 == 0 and spells[j // 3] + 1 == spells[j]:
#         trace.append(j // 3)
#         j = j // 3
#
# trace.reverse()
# print(*trace)
# print(time.time() - start_time)
# def spells(value, finish, tr=None):
#     if tr is None:
#         tr = [value]
#     if value == finish:
#         return tr
#     if value > finish:
#         return [0] * (finish + 1)
#     return min([spells(value * 3, finish, tr + [value * 3]),
#                 spells(value * 2, finish, tr + [value * 2]),
#                 spells(value + 1, finish, tr + [value + 1])], key=len)
#
# start_time = time.time()
# res = spells(1, 100)
# print(len(res) - 1)
# print(*res)
# print(time.time() - start_time)
# def min_func(x):
#     return x[1]
#
# def max_func(x):
#     return int(x)
#
#
# print(max(["11", "1", "3"], key=max_func))
# print(min([(0, 5), (3, 2)], key=min_func))
# print(min([[0, 1, 2], [4, 5, 6], [2, 7, 8, 2]], key=len))


# def Levenstein(s, g):
#     n = len(s) + 1
#     m = len(g) + 1
#     weights = [[i + j for j in range(m)] for i in range(n)]
#     # for i in range(1, n):
#     #     weights[i][0] = i
#     # for j in range(1, m):
#     #     weights[0][j] = j
#     for i in range(1, n):
#         for j in range(1, m):
#             if s[i - 1] == g[j - 1]:
#                 weights[i][j] = weights[i - 1][j - 1]
#             else:
#                 weights[i][j] = min(weights[i - 1][j],
#                         weights[i][j - 1],
#                         weights[i - 1][j - 1]) + 1
#     return weights[-1][-1]

# def hit(a, b):
#     x1, y1 = a
#     x2, y2 = b
#     return x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1)
#
#
# def check_fit(i, j, pos):
#     for k in range(i):
#         if hit((i, j), (k, pos[k])):
#             return False
#     return True
#
#
# def back_track_queen(i=0, pos=None):
#     if i == 8:
#         return True, pos
#     if pos is None:
#         pos = [-1 for j in range(8)]
#     for j in range(8):
#         if check_fit(i, j, pos):
#             pos[i] = j
#             res, pos = back_track_queen(i + 1, pos)
#             if res:
#                 return res, pos
#     pos[i] = -1
#     return False, pos
#
#
# print(*back_track_queen()[1])


def fact(n):
    if n == 0:
        return 1
    return fact(n - 1) * n

print(fact(12))