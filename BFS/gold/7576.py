# 토마토
from collections import deque


def bfs(start):
    day = 0
    Q = deque()
    for i, j in start:
        visited[i][j] = 1
        Q.append((i, j))
    
    while len(Q) != 0:
        for _ in range(len(Q)):
            i, j = Q.popleft()
            for di, dj in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                ni = i + di
                nj = j + dj
                if 0 <= ni <= N - 1 and 0 <= nj <= M - 1:
                    if not visited[ni][nj] and box[ni][nj] == 0:
                        box[ni][nj] = 1
                        visited[ni][nj] = 1
                        Q.append((ni, nj))
        if len(Q) != 0:
            day += 1
        

    return day

M, N = map(int, input().split())
box = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
start = []

for i in range(N):
    l = list(map(int, input().split()))
    for j, k in enumerate(l):
        box[i][j] = k
        if k == 1:
            start.append((i, j))

answer = bfs(start)
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            answer = -1
print(answer)