import sys

sys.stdin = open('boj14425.txt')

N, M = map(int, input().split())

S = []
for i in range(N):
    n = input()
    S.append(n)

cnt = 0
for ii in range(M):
    m = input()
    if m in S:
        cnt += 1
print(cnt)