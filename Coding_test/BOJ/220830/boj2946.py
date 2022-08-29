TC = int(input())
numbers = list(map(int, input().split()))
cnt = 0 
result = 0

for i in range(TC - 1):
    if numbers[i] < numbers[i + 1]:
        cnt += numbers[i + 1] - numbers[i] 
    else:
        if cnt > result:
            result = cnt
            cnt = 0
        else:
            cnt = 0
if cnt > result:
    result = cnt
print(result)

