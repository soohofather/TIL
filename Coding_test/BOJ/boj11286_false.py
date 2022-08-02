import sys
import heapq

sys.stdin = open('boj11286.txt')

T = int(input())

heap = []

for i in range(T):
    number = int(input())
    if number == 0:
        if len(heap) == 0:
            print(0)
        elif len(heap) == 1:
            print(heapq.heappop(heap))
        elif min(heap) == min(abs(heap)):
            print(heapq.heappop(heap))
        elif min(heap) == -1:
            print(heapq.heappop(heap))
        elif min(heap) == -2:
            if heap not in -1 and heap not in 1:
                print(heapq.heappop(heap))
            elif heap in -1:
                
                heapq.heappop(heap)
 

    else:
        heapq.heappush(heap, number)
