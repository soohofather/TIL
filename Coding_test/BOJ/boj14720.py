
n = int(input())
store = list(map(int, input().split()))

count = 0

for i in range(n):
    if (store[i] == count % 3):             # 3으로 나눈 나머지와 같을경우에 +1을 하는 반복문
        count += 1                          # 맨처음 0으로 설정하여 나머지가 3인경우에 처음 1카운트 시작, 즉 0부터 시작하게 만듬
                                            # 카운트가 0, 1, 2 에 맞춰서 내려오는 숫자가 0, 1, 2일때 카운트가 올라가고
print(count)                                # 카운트가 3, 4, 5가 나머지 순서가 0, 1, 2니까 내려오는 숫자가 0, 1, 2일때 카운트가 올라감.
                                            # 전체 카운트는 우유를 마신 숫자.