import sys
import random

sys.stdin = open("test.txt")

height = []

for _ in range(9):
    height.append(int(input()))

random_height = []

while sum(random_height) != 100:
    random_height = random.sample(height, 7)
random_height.sort()
for i in random_height:
    print(i)