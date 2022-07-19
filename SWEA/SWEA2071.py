T = int(input())

for t in range(1, T + 1):
    List=list(map(int, input().split()))

    print(f"#{t} {round(sum(List)/len(List))}")