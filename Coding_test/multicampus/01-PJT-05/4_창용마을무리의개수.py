import sys

sys.stdin = open("_창용마을무리의개수.txt")

TC = int(input())

for tc in range(1, TC + 1):

    N, M = map(int, input().split())

    list_ = [[] for _ in range(N + 1)]

    for i in range(M):
        a, b = map(int, input().split())
        list_[a].append(b)
        list_[b].append(a)

    visited = []

    def dfs(start):
        if start in visited:
            return
        visited.append(start)
        for i in list_[start]:
            dfs(i)

    cnt = 0

    for ii in range(1, N + 1):
         if ii not in visited:
            cnt += 1
            dfs(ii)
    print(f'#{tc}', cnt)