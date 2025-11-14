# 경로 찾기
import sys

sys.setrecursionlimit(10**6)


def dfs(i):
    for j in adj[i]:
        if not visited[j]:
            visited[j] = 1
            dfs(j)

N = int(input())
adj = {i: [] for i in range(1, N + 1)}
for i in range(1, N + 1):
    for k, j in enumerate(map(int, input().split())):
        if j == 1:
            adj[i].append(k + 1)

for i in adj:
    visited = [0] * (N + 1)
    if len(adj[i]) > 0:
        dfs(i)
        for j in visited[1:]:
            print(f'{j} ', end='')
        print()
    if len(adj[i]) == 0:
        print("0 " * N)