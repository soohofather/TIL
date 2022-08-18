import sys
import heapq

input = sys.stdin.readline

T = int(input())

heap = []
heapq.heapify(heap)

for i in range(T):
    number = int(input())
    if number == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, number)
