import sys

sys.stdin = open('test.txt')

numbers_A = list(map(int, input().split()))
numbers_B = list(map(int, input().split()))

count_A = 0
count_B = 0
last_winner = 'D'


for i in range(10):
    if numbers_A[i] > numbers_B[i]:
        count_A += 3
        last_winner = 'A'
    elif numbers_A[i] < numbers_B[i]:
        count_B += 3
        last_winner = 'B'
    else:
        count_A += 1
        count_B += 1
else:
    if count_A > count_B:
        last_winner = 'A'
    elif count_A < count_B:
        last_winner = 'B'
print(count_A, count_B)
print(last_winner)

