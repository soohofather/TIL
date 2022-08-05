import sys

sys.stdin = open('boj11945.txt')

N, M = map(int, input().split())

for i in range(N):
    print(input()[::-1])
