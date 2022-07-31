import sys

sys.stdin = open('boj10818.txt')

T = input()

numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))