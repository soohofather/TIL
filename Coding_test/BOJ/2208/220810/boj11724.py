import sys

sys.stdin = open('boj11724.txt')

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = []


def dfs(a):
    if a in visited:
        return
    visited.append(a)
    for ii in graph[a]:
        dfs(ii)

cnt = 0

for iii in range(1, N + 1):
    if iii not in visited:
        dfs(iii)
        cnt += 1

print(cnt)