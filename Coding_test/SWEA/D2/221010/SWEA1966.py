import sys
import heapq

sys.stdin = open("test.txt")

TC = int(input())

for _ in range(1, TC + 1):

    n = int(input())

    n_list = list(map(int, input().split()))

    result = []

    for i in n_list:
        heapq.heappush(result, i)
    print(f"#{_}", end=" ")

    for ii in range(len(result)):
        n = heapq.heappop(result)
        print(n, end=" ")
    print()
