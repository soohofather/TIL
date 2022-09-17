p, k = map(int, input().split())

result = 1

while k != p:
    if k != p:
        k += 1
        result += 1
print(result)


