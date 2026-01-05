# 동전 2

def solve():
    for i in range(N):
        dp[i][0] = 0
        for j in range(K + 1):
            jj = j + coin[i]
            if jj <= K:
                dp[i][jj] = min(dp[i][jj], dp[i][j] + 1)
            dp[i + 1][j] = dp[i][j]

N, K = map(int, input().split())
coin = []
for i in range(N):
    c = int(input())
    coin.append(c)

inf = 100000 + 1
dp = [[inf] * (K + 1) for _ in range(N + 1)]
solve()
result = dp[N - 1][K]
if result == inf:
    result = -1
print(result)