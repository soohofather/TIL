T = int(input())
list = list(map(int, input().split()))
result = []
new_result = []

for i in range(0, T - 1):
    if list[i + 1] > list[i]:
        result.append(list[i])
    elif list[i + 1] < list[i]:
        result.append(list[i])
        if len(result) <= 1:
            result = []
        else:
            new_result.append(result[len(result) - 1] - result[0])
            result = []
    elif list[i + 1] == list[i]:
        if len(result) <= 1:
            result = []
        else:
            new_result.append(result[len(result) - 1] - result[0])
            result = []        
else:
    if list[T - 1] > list[T - 2]:
        result.append(list[T - 1])
        new_result.append(result[len(result) - 1] - result[0])

print(max(new_result) if new_result != [] else 0)