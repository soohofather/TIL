T = int(input())

for _ in range(T):

    N, M = map(int, input().split())

    find_0 = []

    for i in range(N, M + 1):
        for ii in range(len(str(i))):
            find_0.append(str(i)[ii])
    print(find_0.count('0'))