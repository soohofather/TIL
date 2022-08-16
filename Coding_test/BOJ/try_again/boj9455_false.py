
import sys

sys.stdin = open('boj9455.txt')

n, m = map(int, input().split())

box = []

for i in range(n):
    numbers = list(map(int, input().split()))
    box.append(numbers)

right_box = []
new_box = []

for ii in range(m):
    right_box.append([0]*n)

for iii in range(m):
    for iiii in range(n):
        right_box[iii][iiii] = (box[iiii][iii])
    new_box.append(right_box[iii][::-1])

result = 0

for iiiii in range(m):
    a = new_box[iiiii].count(1)
    for b in range(n):
        if new_box[iiiii][b] == 1:
            result += b
    print(a, result)
    result = 0
