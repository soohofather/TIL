A, B = map(int, input().split())
C = []

for i in range(B):
    for ii in range(i):
        C.append(i)
print(sum(C[A-1:B]))



# 1 + 2 + 3 + ... + 46을 하면 라인수가 1000을 넘음, 문제에서 첫째줄의 구간이 1000라인을 넘지 않는다고 되어있음
# N = 0                 
# cnt = 0

# while N < 1000:
#     cnt += 1
#     N += cnt
# print(cnt)