# def heapify(A):
#     for i in range(len(A))[::-1]:
#         j = 2 * i + 1
#         k = 2 * i + 2
#         while j < len(A):
#             c = j
#             if k < len(A) and A[j] > A[k]:
#                 c = k
#             if A[i] > A[c]:
#                 A[i], A[c] = A[c], A[i]
#                 i = c
#             else:
#                 break
#             j = 2 * i + 1
#             k = 2 * i + 2
#
# def heap_pop(A):
#     res = A[0]
#     if len(A) == 1:
#         return res
#     A[0] = A.pop()
#     i = 0
#     j = 2 * i + 1
#     k = 2 * i + 2
#     while j < len(A):
#         c = j
#         if k < len(A) and A[j] > A[k]:
#             c = k
#         if A[i] > A[c]:
#             A[i], A[c] = A[c], A[i]
#             i = c
#         else:
#             break
#         j = 2 * i + 1
#         k = 2 * i + 2
#     return res
#
#
# N, k = [int(x) for x in input().split()]
# A = [int(x) for x in input().split()]
# heapify(A)
# res = []
# for i in range(k):
#     res.append(heap_pop(A))
# print(*res)


# N, k = [int(x) for x in input().split()]
# A = [int(x) for x in input().split()]
#
# def shrink(A, size):
#     while len(A) >= size:
#         prev_A = A
#         pivot = A[0]
#         A = [x for x in A if x < pivot]
#     return prev_A
#
#
# A = shrink(A, k)
# print(*sorted(A)[:k])


def backpack(A, w_0):
    matrix = [[False for j in range(w_0 + 1)] for i in range(len(A) + 1)]
    matrix[0][0] = True
    for i in range(len(A)):
        for j in range(w_0 + 1):
            matrix[i + 1][j] = matrix[i][j]
            if j - A[i] >= 0 and matrix[i][j - A[i]]:
                matrix[i + 1][j] = True
    for j in range(w_0 + 1)[::-1]:
        for i in range(len(A) + 1)[::-1]:
            if matrix[i][j]:
                return j


print(backpack([5, 3, 2, 4, 3], 16))











