T = int(input())
for _ in range(T):

    S = int(input())

    option_ = int(input())

    while option_ > 0:
        a, b = map(int, input().split())
        S += a * b
        option_ -= 1
        
    print(S)