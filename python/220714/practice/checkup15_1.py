fruit = input()
result = 0

for findyou in fruit:
    if findyou == 'a':
        break
    result += 1
else:
    result = -1
    
print(result)