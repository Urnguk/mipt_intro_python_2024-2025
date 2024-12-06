def stairs():
    n = int(input())
    A = [int(x) for x in input().split()]
    D = dict()
    res = 0
    for i in range(len(A)):
        res += sum([D[key] * key for key in D if key < A[i]])
        if A[i] not in D:
            D[A[i]] = 1
        else:
            D[A[i]] += 1
    return res


t = int(input())
answers = []
for i in range(t):
    answers.append(stairs())
print(*answers, sep="\n")
