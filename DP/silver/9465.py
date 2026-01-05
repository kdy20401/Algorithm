# 스티커

def solution(sticker, N):
    # dp[n][0]: n번째 열까지 스티커를 땠고, n번째 열에서는 아무 스티커를 때지 않았을 때 점수 최대값
    # dp[n][1]: n번째 열까지 스티커를 땠고, n번째 열에서 위 스티커를 땠을 때 점수 최대값
    # dp[n][2]: n번째 열까지 스티커를 땠고, n번째 열에서 아래 스티커를 땠을 때 점수 최대값
    dp = [[0] * 3 for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][0] = max(max(dp[i - 1][0], dp[i - 1][1]), dp[i - 1][2])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + sticker[1][i - 1]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + sticker[0][i - 1]

    return max(max(dp[N][0], dp[N][1]), dp[N][2])

T = int(input())
while T:
    N = int(input())
    sticker = []
    for _ in range(2):
        row = list(map(int, input().split()))
        sticker.append(row)
    answer = solution(sticker, N)
    print(answer)
    T -= 1

    