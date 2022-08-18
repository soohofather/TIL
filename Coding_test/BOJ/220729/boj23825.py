S, A = map(int, input().split())

if S >= A:                                  # 1개 만들때, A 2개 B 2개필요하니까 .. 둘중에 작은 숫자를.. 2로 나눈 그 갯수가.. 전체에서 만들수잇는 갯수다..
    print(A // 2)
else:
    print(S // 2)