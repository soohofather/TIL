import sys

sys.stdin = open('test.txt')


n = int(input())

maraton = {}

for _ in range(n):
    saram = input()

    if saram not in maraton:
        maraton[saram] = 1
    else:
        maraton[saram] += 1

for __ in range(n-1):
    out_saram = input()
    maraton[out_saram] -= 1

for i in maraton:
    if maraton[i] != 0:
        print(i)