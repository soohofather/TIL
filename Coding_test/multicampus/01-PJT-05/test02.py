import sys

sys.stdin = open("test.txt")

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

    for ii in range(1, len(list_)):
        for iii in list_[ii]:
            print(ii,iii)
            if iii not in visited:
                cnt += 1
                dfs(iii)
    print(f'#{tc}', cnt)