import sys

sys.stdin = open('boj14425.txt')

N, M = map(int, input().split())

S = []
for i in range(N):
    n = input()
    S.append(n)

T = []
for ii in range(M):
    m = input()
    T.append(m)

cnt = 0
for iii in T:
    if iii in S:
        cnt += 1
print(cnt)