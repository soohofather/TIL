import sys

sys.stdin = open('boj2167.txt')

N, M = map(int, input().split())

numbers = []

for a in range(N):
    numbers.append(list(map(int, input().split())))

K = int(input())

for b in range(K):
    i, j, x, y = map(int, input().split())
    result = 0
    for c in range(i - 1, x):      
        for d in range(j - 1, y):       
            result += numbers[c][d]     
    print(result)          