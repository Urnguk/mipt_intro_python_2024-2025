from random import randrange
# def bin_search(A, value):
#     left = 0
#     right = len(A) - 1
#
#     while left <= right:
#         middle = (left + right) // 2
#         if A[middle] == value:
#             return True
#         if value < A[middle]:
#             right = middle - 1
#         else:
#             left = middle + 1
#     return False
#
#
# A = [int(x) for x in input().split()]
# A.sort()
# x = int(input())
#
# if bin_search(A, x):
#     print("yes")
# else:
#     print("no")


# def merge(A, B):
#     res = []
#     i = 0
#     j = 0
#     while i < len(A) and j < len(B):
#         if A[i] <= B[j]:
#             res.append(A[i])
#             i += 1
#         else:
#             res.append(B[j])
#             j += 1
#     res += A[i:] + B[j:]
#     return res

# def merge(A, B):
#     res = []
#     i = 0
#     j = 0
#     while i < len(A):
#         if A[i] > B[j]:
#             A, B = B, A
#             i, j = j, i
#         res.append(A[i])
#         i += 1
#     res += A[i:] + B[j:]
#     return res


# A = [int(x) for x in input().split()]
# B = [int(x) for x in input().split()]
# A.sort()
# B.sort()
#
# print(*merge(A, B))


# def mergesort(A):
#     if len(A) < 2:
#         return A
#     mid = len(A) // 2
#     left = A[:mid]
#     right = A[mid:]
#     return merge(mergesort(left), mergesort(right))
#
#
# print(mergesort([2, 7, 0, -8, 9]))


# def qsort(A, left=0, right=None):
#     if right is None:
#         right = len(A) - 1
#     if left >= right:
#         return
#     i = left
#     j = right
#     pivot = A[left]
#     while i <= j:
#         while A[i] < pivot:
#             i += 1
#         while A[j] > pivot:
#             j -= 1
#         if i <= j:
#             A[i], A[j] = A[j], A[i]
#             i += 1
#             j -= 1
#     qsort(A, left, j)
#     qsort(A, i, right)
#
#
# A = [int(x) for x in input().split()]
# qsort(A)
# print(*A)

def heap_add(A, value):
    A.append(value)
    i = len(A) - 1
    while i > 0 and A[i] > A[(i - 1) // 2]:
        A[i], A[(i - 1) // 2] = A[(i - 1) // 2], A[i]
        i = (i - 1) // 2


# def heap_pop(A):
#     res = A[0]
#     A[0] = A.pop()
#     i = 0
#     j = 2 * i + 1
#     k = 2 * i + 2
#     while i < len(A):
#         if k < len(A):
#             if A[j] >= A[k] and A[j] >= A[i]:
#                 A[i], A[j] = A[j], A[i]
#                 i = j
#             elif A[k] >= A[j] and A[k] >= A[i]:
#                 A[i], A[k] = A[k], A[i]
#                 i = k
#             else:
#                 return
#         else:
#             if A[i] < A[j]:
#                 A[j], A[i] = A[i], A[j]
#                 i = j
#         j = 2 * i + 1
#         k = 2 * i + 2
#     return res

# def heap_pop(A):
#     res = A[0]
#     if len(A) == 1:
#         return res
#     A[0] = A.pop()
#     i = 0
#     j = 2 * i + 1
#     k = 2 * i + 2
#     while j < len(A):
#         if k < len(A):
#             if A[i] < max(A[j], A[k]):
#                 if A[j] >= A[k]:
#                     A[i], A[j] = A[j], A[i]
#                     i = j
#                 else:
#                     A[i], A[k] = A[k], A[i]
#                     i = k
#             else:
#                 break
#         else:
#             if A[i] < A[j]:
#                 A[j], A[i] = A[i], A[j]
#                 i = j
#             else:
#                 break
#         j = 2 * i + 1
#         k = 2 * i + 2
#     return res

def heap_pop(A):
    res = A[0]
    if len(A) == 1:
        return res
    A[0] = A.pop()
    i = 0
    j = 2 * i + 1
    k = 2 * i + 2
    while j < len(A):
        c = j
        if k < len(A) and A[j] < A[k]:
            c = k
        if A[i] < A[c]:
            A[i], A[c] = A[c], A[i]
            i = c
        else:
            break
        j = 2 * i + 1
        k = 2 * i + 2
    return res


# A = []
# for i in range(15):
#     heap_add(A, randrange(0, 10))

def heap_print(A):
    start = 0
    l = 1
    while start + l < len(A):
        print(*A[start:start + l])
        start = start + l
        l *= 2
    print(*A[start:])


# heap_print(A)
# heap_pop(A)
# heap_print(A)


def heap_sort(A):
    heap = []
    for element in A:
        heap_add(heap, element)
    for i in range(len(A)):
        A[len(A) - 1 - i] = heap_pop(heap)


A = [randrange(0, 10) for i in range(25)]
heap_sort(A)
print(*A)