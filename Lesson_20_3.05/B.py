from functools import reduce


def optim_prefix(s):
    res = [0 for i in range(len(s))]

    for i in range(1, len(s)):
        j = res[i - 1]
        while j > 0 and s[i] != s[j]:
            j = res[j - 1]
        if s[i] == s[j]:
            res[i] = j + 1
    return res


def stitch(s, g):
    min_len = min(len(s), len(g))
    suff_s = s[-min_len:]
    kmp = g + "#" + suff_s
    overlap = optim_prefix(kmp)[-1]
    return s + g[overlap:]


def solve():
    _ = input()
    print(reduce(stitch, input().split()))


solve()
