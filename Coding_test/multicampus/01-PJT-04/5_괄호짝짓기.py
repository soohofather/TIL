import sys

sys.stdin = open("_괄호짝짓기.txt")

for _ in range(1, 11):
    T = int(input())

    gwalho = input()

    gwalho_1 = []
    gwalho_2 = []
    gwalho_3 = []
    gwalho_4 = []
    result = 1

    for i in range(T):
        if result == 0:
            print(f'#{_}', 0)
            break
        else:
            if gwalho[i] == '(':
                gwalho_1.append(gwalho[i])
            elif gwalho[i] == '[':
                gwalho_2.append(gwalho[i])
            elif gwalho[i] == '{':
                gwalho_3.append(gwalho[i])
            elif gwalho[i] == '<':
                gwalho_4.append(gwalho[i])
            elif gwalho[i] == ')':
                if len(gwalho_1) == 0:
                    result = 0
                else:
                    gwalho_1.pop()
            elif gwalho[i] == ']':
                if len(gwalho_2) == 0:
                    result = 0
                else:
                    gwalho_2.pop()
            elif gwalho[i] == '}':
                if len(gwalho_3) == 0:
                    result = 0
                else:
                    gwalho_3.pop()
            elif gwalho[i] == '>':
                if len(gwalho_4) == 0:
                    result = 0
                else:
                    gwalho_4.pop()
    else:
        if result == 0:
            print(f'#{_}', 0)
        else:
            if len(gwalho_1) == 0 and len(gwalho_2) == 0 and len(gwalho_3) == 0 and len(gwalho_4) == 0:
                print(f'#{_}', 1)
            else:
                print(f'#{_}', 0)