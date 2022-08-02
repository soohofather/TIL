import sys

sys.stdin = open('boj1269.txt')

M, N = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A.difference(B)) + len(B.difference(A)))