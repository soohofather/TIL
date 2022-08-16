
import sys

sys.stdin = open('test.txt')

T = int(input())

log = set()
sum = 0

for i in range(T):
    gomgom = input()
    if gomgom == 'ENTER':
        continue
    elif gomgom in log:
        continue
    else:
        log.add(gomgom)
        sum += 1

print(sum)