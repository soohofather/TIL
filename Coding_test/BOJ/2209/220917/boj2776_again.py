TC = int(input())

for _ in range(TC):

    a_TC = int(input())
    a_numbers = set(map(int, input().split()))
    b_TC = int(input())
    b_numbers = list(map(int, input().split()))

    for i in b_numbers:
        if i in a_numbers:
            print(1)
        else:
            print(0)
