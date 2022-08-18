import sys

sys.stdin = open('boj1269.txt')

M, N = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result_A = []
result_B = []

for a in A:
    if a not in B:
        result_A.append(a)
else:
    for b in B:
        if b not in A:
            result_B.append(b)
print(len(result_A) + len(result_B))
