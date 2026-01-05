# 적록색약
import sys

sys.setrecursionlimit(10**5)

def dfs(i, j, red_green_flag):
    cur_color = grid[i][j]
    visited[i][j] = 1
    for di, dj in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N:
            adj_color = grid[ni][nj]
            if red_green_flag == 0:
                if cur_color == adj_color and not visited[ni][nj]:
                    dfs(ni, nj, red_green_flag)
            else:
                if cur_color == 'B':
                    if cur_color == adj_color and not visited[ni][nj]:
                        dfs(ni, nj, red_green_flag)
                else:
                    if (adj_color == 'R' or adj_color == 'G') and not visited[ni][nj]:
                        dfs(ni, nj, red_green_flag)


N = int(input())
grid = []
visited = [[0] * N for _ in range(N)]
for _ in range(N):
    s = input()
    grid.append(s)

c1, c2 = 0, 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, 0)
            c1 += 1

visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, 1)
            c2 += 1

print(c1, c2)