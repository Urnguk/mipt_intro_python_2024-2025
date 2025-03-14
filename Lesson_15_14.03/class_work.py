def z(s):
    max_start = -1
    max_finish = -1
    res = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        if i <= max_finish:
            k = i - max_start
            if res[k] < max_finish - i - 1:
                res[i] = res[k]
                continue
            else:
                j = res[k] - 1
        else:
            j = 0
        while i + j < len(s) and s[j] == s[i + j]:
            res[i] = j + 1
            j += 1
        if i + j > max_finish:
            max_finish = i + j
            max_start = i
    return res


def prefix(s):
    res = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        for k in range(1, i + 1):
            if s[:k] == s[i - k + 1: i + 1]:
                res[i] = k

    return res

def optim_prefix(s):
    res = [0 for i in range(len(s))]

    for i in range(1, len(s)):
        j = res[i - 1]
        while j > 0 and s[i] != s[j]:
            j = res[j - 1]
        if s[i] == s[j]:
            res[i] = j + 1
    return res


s = "abacabadabacabac"
print(*s)
print(*z(s))
print(*prefix(s))
print(*optim_prefix(s))
