import sys

input = sys.stdin.readline

TC = int(input())

greeting = set()
cnt = 0

for _ in range(TC):
    chat = str(input().rstrip())
    if chat == 'ENTER':
        greeting.clear()
    else:
        if chat not in greeting:
            greeting.add(chat)
            cnt += 1
print(cnt)
