import sys

sys.stdin = open('test.txt')

chess_pan = []

for i in range(8):                              # 받은 정보를 전체 chess_pan에 넣음
    chess_pan.append(input())

result = 0

for ii in range(8):
    for iii in range(8):
        if (ii + iii) % 2 != 0:                 # 하얀색 체스판 위치가 행 열의 합이 짝수인것을 확인하고,
            continue                            # 행 열의 합이 홀수면 그냥 패스
        else:
            if chess_pan[ii][iii] == 'F':       # 행 열의 합이 짝수인데, F면 result에 +1
                result += 1
print(result)
