# 음식물 피하기
import sys


sys.setrecursionlimit(10**5)

def dfs(r, c):
    global size
    visited[r][c] = 1

    drs = [-1, 1, 0, 0]
    dcs = [0, 0, -1, 1]
    for dr, dc in zip(drs, dcs):
        nr = r + dr
        nc = c + dc
        if nr <= 0 or nr > N or nc <= 0 or nc > M:
            continue
        if grid[nr][nc] == 1 and not visited[nr][nc]:
            size += 1
            dfs(nr, nc)


N, M, K = map(int, input().split())
grid = [[0] * (M + 1) for _ in range(N + 1)]
visited = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    grid[r][c] = 1

max_size = 1
size = 1
for r in range(1, N + 1):
    for c in range(1, M + 1):
        if grid[r][c] == 1 and not visited[r][c]:
            # print(f'dfs({r}, {c}) starts')
            dfs(r, c)
            # print(f'size: {size}')
            max_size = max(max_size, size)
            size = 1

print(max_size)