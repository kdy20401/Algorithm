# DFS와 BFS
import sys
from collections import deque


def dfs(s):
    print(s, end=' ')
    visited[s] = 1
    for v in adj[s]:
        if not visited[v]:
            dfs(v)

def bfs(s):
    Q = deque()
    visited[s] = 1
    Q.append(s)

    while len(Q) != 0:
        next = [Q.popleft() for _ in range(len(Q))]
        for u in next:
            print(u, end=' ')
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = 1
                    Q.append(v)

N, M, V = map(int, input().split())
visited = [0] * (N + 1)
adj = {i + 1: [] for i in range(N)}

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(N):
    adj[i + 1] = sorted(adj[i + 1])

# print(adj)

dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)