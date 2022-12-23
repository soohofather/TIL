n = int(input())

delays = list(map(int, input().split()))

delays.sort()

result = 0
time = 0

for i in range(n):
    time += delays[i]
    result += time
print(result)
