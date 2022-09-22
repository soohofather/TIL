TC = int(input())

for _ in range(TC):

    a, b = map(int, input().split())

    box = []

    for _ in range(a):
        numbers = list(map (int, input().split()))
        box.append(numbers)

    new_box = [[] for _ in range(b)]

    for _ in range(len(box)):
        box_last = box.pop()
        for i in range(len(box_last)):
            new_box[i].append(box_last[i])

    cnt = 0

    for j in new_box:
        floor = 0
        for jj in range(a):
            if j[jj] == 1:
                cnt += jj - floor
                floor += 1
    print(cnt)