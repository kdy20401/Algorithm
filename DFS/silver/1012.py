# 유기농 배추
import sys
sys.setrecursionlimit(1000000)


def dfs(x, y):
    global visited, grid # 없어도 됨
    visited[x][y] = 1
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= len(visited[0]) or ny < 0 or ny >= len(visited):
            continue
        if grid[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)    


T = int(input())
while T:
    width, height, num_cabbage = map(int, input().split())
    grid = [[0] * 50 for _ in range(50)]
    visited = [[0] * 50 for _ in range(50)]
    for _ in range(num_cabbage):
        x, y = map(int, input().split())
        grid[x][y] = 1

    num_worm = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                num_worm += 1

    print(num_worm)
    T -= 1
