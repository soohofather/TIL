import sys

input = sys.stdin.readline

TC = int(input())

greeting = set()
cnt = 0

for i in range(TC):
    chat = input()
    if chat == 'ENTER':
        cnt += len(greeting)
        greeting = set()
    else:
        greeting.add(chat)


        
cnt += len(greeting)
print(cnt)
