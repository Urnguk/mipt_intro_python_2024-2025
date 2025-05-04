def optim_prefix(s):
    res = [0 for i in range(len(s))]

    for i in range(1, len(s)):
        j = res[i - 1]
        while j > 0 and s[i] != s[j]:
            j = res[j - 1]
        if s[i] == s[j]:
            res[i] = j + 1
    return res


def cnt_unique_cont_subs(s):
    res = 0
    for i in range(len(s)):
        suf = s[i:]
        pref = optim_prefix(suf)
        res += len(suf) - max(pref)
    return res


def solve():
    s = input()
    print(cnt_unique_cont_subs(s))


solve()