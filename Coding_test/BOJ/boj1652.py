
import sys

sys.stdin = open('boj1652.txt')

N = int(input())                # 맨 첫줄 길이를 받고,

condo = []

for i in range(N):              # 구조를 만들고~
    packs = input()
    condo.append(packs)

garo = 0

for ii in condo:                # 위에서 만든구조에서 각 라인을 X로 나눠서 
    for iii in ii.split('X'):   # 그 나눈것이 2가 넘는다면 자리 1 추가
        if len(iii) >= 2:
            garo += 1

sero = 0
sero_jari = ''

for iiii in range(N):                       # 열은 열 먼저 만들어서 sero_jari에 넣고
    for iiiii in range(N):                  # 넣은 것을 위에 행과 같은 방법으로
        sero_jari += condo[iiiii][iiii]     # 각 라인을 X로 나눠서 숫자가 2인 경우에 1 추가
    for iiiiii in sero_jari.split('X'):     
        if len(iiiiii) >= 2:
            sero += 1
        sero_jari = ''

print(garo, sero)