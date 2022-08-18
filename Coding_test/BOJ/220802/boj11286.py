import sys
import heapq

sys.stdin = open('boj11286.txt')

T = int(input())

heap = []

for i in range(T):
    number = int(input())
    if number == 0:
        if not heap:                                    # 만약에 heap이 아무것도 없다면, 
            print(0)                                    # 프린트 0
        else:   
            print(heapq.heappop(heap)[1])               # 아무것도 없는게 아니라면 제일 왼쪽거를 빼는데 (절대값, 내려온값)일테니까 [1]을 넣어서 내려온값을 출력
    else:
        heapq.heappush(heap, (abs(number), number))     # 내려오는 수가 0이 아니면 그 숫자를 (절대값, 내려온 값)으로 저장
                                                        # 왜냐하면, 이렇게하면 절대값순으로 정렬이 되고 추가로 두번째 내려온 값도 정렬에 가담하게 되어서
                                                        # 절대값이 같아도 내려온값이 작은 숫자가 더 왼쪽으로 가게되어, pop할때 빠져나오게 됨.
