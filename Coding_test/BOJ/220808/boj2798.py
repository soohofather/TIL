
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

for i in range(N - 2):
    for ii in range(i + 1, len(numbers)-1):
        for iii in range(ii + 1, len(numbers)):
            if numbers[i] + numbers[ii] + numbers[iii] > M:
                continue
            elif numbers[i] + numbers[ii] + numbers[iii] > result:
                result = numbers[i] + numbers[ii] + numbers[iii]
    if result == M:
        break
print(result)

