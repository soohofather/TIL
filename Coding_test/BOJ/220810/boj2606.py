import sys

sys.stdin = open('boj2606.txt')

n = int(input())
m = int(input())

# 인접 리스트 작성
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 컴퓨터에 방문 했는지 안했는지 확인하는 것
visited = [False] * (n + 1)

# 1번컴퓨터가 바이러스의 시작이라 1번 설정
def dfs(start):
    # 데이터를 넣고 빼고 할 공간 설정
    stack = [start]
    # 시작컴퓨터인 1번은 방문하였으니 True로 변경
    visited[start] = True

    while stack != []:
        cur = stack.pop()
        # 처음 시작인 컴퓨터와 연결된 컴퓨터 각각을 탐색해서, visitied가 false인지 true인지봄
        # 그리고 false면 true로 바꾸고 stack에다가 해당 데이터를 넣음. 스택에 넣어서 또 연결된 걸 확인 하게 됨
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
    return sum(visited) - 1
print(dfs(1))