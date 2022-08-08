T = int(input())

for _ in range(1, T+1):

    score = list(map(int, input().split()))
    student_ = score.pop(0)
    score.sort()
    gap = 0

    for i in range(student_ - 1):
        if score[i+1] - score[i] > gap:
            gap = score[i+1] - score[i]
    print('Class', _)
    print(f'Max {max(score)},', f'Min {min(score)},', f'Largest gap {gap}')