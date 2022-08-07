from itertools import count
import sys

sys.stdin = open("_최빈수구하기.txt")

T1 = int(input())

for i in range(T1):

    T2 = input()
    numbers = list(map(int, input().split()))     
    counting = 0
    result = 0

    for i in range(0, 101):   
        if numbers.count(i) > counting:
            counting = numbers.count(i)
            result = 0
            result += i
        elif numbers.count(i) == counting:
            if i > result:
                result = 0
                result += i

    print(f'#{T2}', result)
