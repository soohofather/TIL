import sys

sys.stdin = open('boj3052.txt')

C = []

for i in range(0,10):
    
    A = int(input())
    B = A % 42

    if B not in C:
        C.append(B)
print(len(C))
    
