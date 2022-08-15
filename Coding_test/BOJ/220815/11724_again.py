n, m = map(int, input().split())

numbers = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    numbers[a].append(b)
    numbers[b].append(a)

visited = []

def dfs(start):
    if start in visited:
        return
    visited.append(start)
    for ii in numbers[start]:
        dfs(ii)

cnt = 0

for iii in range(1, n + 1):
    if iii not in visited:
        dfs(iii)
        cnt += 1

print(cnt)

