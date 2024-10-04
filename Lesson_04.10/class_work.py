# def fib(n, memo=None):
#     if memo is None:
#         memo = [-1] * (n + 1)
#     if memo[n] == -1:
#         if n == 0 or n == 1:
#             memo[n] = n
#         else:
#             memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
#     return memo[n]
#
#
# def fib2(n):
#     a, b = 0, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     return b
#
#
# print(fib(50))
# print(fib2(50))

# x = 0
# while True:
#     print(x)
#     x += 1


# prices = [int(x) for x in input().split()]
# sums = [-float("inf") for i in range(len(prices))]
#
# sums[0] = prices[0]
# sums[1] = prices[1] + sums[0]
# for i in range(2, len(sums)):
#     sums[i] = prices[i] + max(sums[i - 1], sums[i - 2])
# print(sums)
#
# sums = [-float("inf") for i in range(len(prices))]
#
# sums[0] = prices[0]
# for i in range(len(sums) - 2):
#     sums[i + 1] = max(prices[i + 1] + sums[i], sums[i + 1])
#     sums[i + 2] = max(prices[i + 2] + sums[i], sums[i + 2])
# sums[-1] = max(prices[-1] + sums[-2], sums[-1])
# print(sums)

# N, M = (int(x) for x in input().split())
# prices = [[int(x) for x in input().split()] for i in range(N)]
# sums = [[prices[i][j] for j in range(M)] for i in range(N)]
#
# for j in range(1, M):
#     sums[0][j] += sums[0][j - 1]
# for i in range(1, N):
#     sums[i][0] += sums[i - 1][0]
# for i in range(1, N):
#     for j in range(1, M):
#         sums[i][j] += max(sums[i - 1][j], sums[i][j - 1])
# print(sums[-1][-1])




# for line in A:
#     print(*line)


# from matplotlib import pyplot as plt
# import pandas as pd
# import numpy as np
#
# data = pd.read_csv("iris_data.csv")
#
# X1 = np.array(data["SepalLengthCm"])
# Y1 = np.array(data["SepalWidthCm"])
# plt.scatter(X1, Y1)
# X1_2 = X1 ** 2
# X1_Y1 = X1 * Y1
# a = ((np.average(X1_Y1) - np.average(X1) * np.average(Y1)) /
#         (np.average(X1_2) - np.average(X1) ** 2))
# b = np.average(Y1) - a * np.average(X1)
# Y_MNK = X1 * a + b
# plt.plot(X1, Y_MNK, color="red")
#
#
# plt.show()

x, y = input().split()
x = int(x)
print(x, type(x))
print(y, type(y))