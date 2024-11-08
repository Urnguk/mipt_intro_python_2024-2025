from time import time
from random import randint


# def find_max_i(A):
#     res = 0
#     for i in range(1, len(A)):
#         if A[i] >= A[res]:
#             res = i
#     return res
#
#
# def selection_sort(A):
#     for i in range(len(A) - 1):
#         j = find_max_i(A[:len(A) - i])
#         f = len(A) - 1 - i
#         A[j], A[f] = A[f], A[j]


# def insertion_sort(A):
#     for i in range(1, len(A)):
#         j = i
#         while 0 < j and A[j - 1] > A[j]:
#             A[j], A[j - 1] = A[j - 1], A[j]
#             j -= 1

def counting_sort(A):
    cnts = [0 for i in range(10)]
    for i in range(len(A)):
        cnts[A[i]] += 1

    res = []
    for i in range(len(cnts)):
        res += [i] * cnts[i]
    return res

A = [randint(0, 9) for i in range(10 ** 6)]
start = time()
A = counting_sort(A)
finish = time()
print(finish - start)
