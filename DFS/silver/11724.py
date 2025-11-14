# 연결 요소의 개수
import sys


sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
adj = {u: [] for u in range(1, N + 1)}
visited = [0] * (N + 1)

def dfs(u):
    visited[u] = 1
    for v in adj[u]:
        if not visited[v]:
            dfs(v)
    return


for _ in range(M):
    u, v = map(int, input().split()) # slow
    u, v = map(int, sys.stdin.readline().split()) # fast
    adj[u].append(v)
    adj[v].append(u)



num_cc = 0
for u in adj:
    if not visited[u]:
        dfs(u)
        num_cc += 1

print(num_cc)