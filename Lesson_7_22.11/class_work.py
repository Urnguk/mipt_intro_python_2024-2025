# A = [2, 6, 2, 7, 8, 9, 3, 3, 4, 5]
# print(list(set(A)))

# S = {4, 6, 7}
# S.add(1)
# S.add(7)
# print(S)
# S.discard(7)
# print(S)
# S.discard(3)
# print(S)
# print(type(S))

# D = dict()
# D["abc"] = 2
# print(D["abc"])
# D["bcd"] = 4
# print(D)
# del D["abc"]
# print(D)

roots = {value ** 2: value for value in range(10)}
x = int(input())
if x in roots:
    print(roots[x])
else:
    print("no integer root")

print(type(roots.keys()))
print(type(roots.values()))

