import sys

sys.stdin = open('boj14425.txt')

N, M = map(int, input().split())

S = []
T = []

for i in range(N):
    n = input()
    S.append(n)
for ii in range(M):
    m = input()
    T.append(m)
print(len(T) - len(set(T)^(set(S)&set(T))))