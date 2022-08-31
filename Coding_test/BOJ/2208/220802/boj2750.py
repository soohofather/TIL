import sys
import heapq


sys.stdin = open('boj2750.txt')

N = int(input())

heap = []

for i in range(N):
    number = int(input())
    heapq.heappush(heap, number)
for ii in range(len(heap)):
    print(heapq.heappop(heap))