def optim_prefix(s):
    res = [0 for i in range(len(s))]

    for i in range(1, len(s)):
        j = res[i - 1]
        while j > 0 and s[i] != s[j]:
            j = res[j - 1]
        if s[i] == s[j]:
            res[i] = j + 1
    return res


def solve():
    res = set()
    n = int(input())
    s = input().strip()
    g = input().strip()
    if s == g:
        print("Random")
        return

    for x in "01":
        kmp = g + "#" + s + x + s
        pref = optim_prefix(kmp)
        m = max(pref)
        if m != len(g):
            continue
        for j in range(len(pref)):
            if pref[j] == m:
                res.add(kmp[j + 1])
    if len(res) == 2:
        print("Random")
    elif "0" in res:
        print("No")
    else:
        print("Yes")


solve()
