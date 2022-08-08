import sys

sys.stdin = open("boj2669.txt")


result = []

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for ii in range(b, d):
            if (i, ii) not in result:
                result.append((i, ii))
print(len(result))