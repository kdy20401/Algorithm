# 1로 만들기
import sys


sys.setrecursionlimit(10**6)

# base case
# f(1) = 0

# after
# f(2) = min(f(1), f(1)) + 1 = 1
# f(3) = min(f(1), f(2)) + 1 = 1
# f(4) = min(f(2), f(3)) + 1 = 2
# f(5) = min(f(4)) + 1 = 3  (5 -> 4 -> 2 -> 1)
# f(6) = min(f(2), f(3), f(5)) + 1 = 2

# # top down
# def f(n):
#     if dp[n] != -1:
#         return dp[n]
    
#     min_result = 1000000
#     if n % 3 == 0:
#         min_result = min(min_result, f(n // 3) + 1)
#     if n % 2 == 0:
#         min_result = min(min_result, f(n // 2) + 1)
#     min_result = min(min_result, f(n - 1) + 1)

#     dp[n] = min_result
#     return dp[n]

# N = int(input()) 
# dp = [-1] * (N + 1)
# dp[1] = 0
# m = f(N)
# print(m)


# bottom up
N = int(input())
dp = [10*7] * (N + 1)
dp[1] = 0

for i in range(1, N + 1):
    if i + 1 < N + 1:
        dp[i + 1] = min(dp[i] + 1, dp[i + 1])
    if i * 2 < N + 1:
        dp[i * 2] = min(dp[i] + 1, dp[i * 2])
    if i * 3 < N + 1:
        dp[i * 3] = min(dp[i] + 1, dp[i * 3])

print(dp[N])
    