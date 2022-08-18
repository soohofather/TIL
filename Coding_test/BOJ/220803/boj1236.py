import sys

sys.stdin = open('boj1236.txt')

N, M = map(int, input().split())        # 첫 줄의 가로, 세로길이를 받고

guard = []

for i in range(N):                      # guard에 전체 데이터('.'혹은 'x')를 쫙~ 넣음
    guard.append(input())

row_cnt = 0

for ii in range(N):                     # 각 행(가로줄)마다 X가 없으면 row_cnt에 +1을 하는 반복문
    if 'X' not in guard[ii]:
        row_cnt += 1 

column_ = []
column_cnt = 0

for iii in range(M):                    # 하나의 열(세로줄)을 만들어서 column_에 넣고, 그 열에 X가 없으면 column_cnt에 +1을 함
    for ii in range(N):                 # 다음 열로 갈때 column_을 다시 빈칸으로 만들어놓음
        column_.append(guard[ii][iii])
    if 'X' not in column_:
        column_cnt += 1
    column_ = []
print(row_cnt if row_cnt > column_cnt else column_cnt)  # 최소 값을 구하는거라 행, 열중에 숫자가 큰 경비원수만 넣으면 나머지 쪽도 해결이 됨.

