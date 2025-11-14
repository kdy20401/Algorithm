# 미로 탐색
from collections import deque


def bfs():
    distance = 1
    Q = deque()
    visited[0][0] = distance
    Q.append((0, 0))

    while len(Q) != 0:
        distance += 1
        for _ in range(len(Q)):
            x, y = Q.popleft()
            for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                    if maze[nx][ny] == 1 and not visited[nx][ny]: 
                        visited[nx][ny] = distance
                        Q.append((nx, ny))


N, M = map(int, input().split())
maze = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    input_str = input()
    for j in range(M):
        if input_str[j] == '1':
            maze[i][j] = 1

bfs()
print(visited[N - 1][M - 1])
# print(visited)