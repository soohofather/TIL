N = int(input())

result = 0
result_cnt = 0
cnt = 0

while result_cnt != N:
    cnt += 1
    if '666' in str(cnt):
        result = cnt
        result_cnt += 1
print(result)
