# 촌수계산
from collections import deque


def bfs(u):
    distance = 0
    Q = deque()
    visited[u] = 1
    Q.append(u)

    while not len(Q) == 0:
        for _ in range(len(Q)):
            u = Q.popleft()
            if u == b:
                return distance
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = 1
                    Q.append(v)
        distance += 1
    
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())

adj = {i: [] for i in range(1, n + 1)}
visited = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

answer = bfs(a)
print(answer)
