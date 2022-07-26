import sys

sys.stdin = open("boj2953.txt")

a = 0
b = 0

for i in range(1, 6):
    point = list(map(int, input().split()))
    if sum(point) > b:
        a = i
        b = sum(point)
    
print(a, b)