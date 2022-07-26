N, A = map(int, input().split())
suyeol = list(map(int, input().split()))
for ii in suyeol:
    if ii < A:
        print(ii, end=' ')
