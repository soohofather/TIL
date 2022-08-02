import sys

sys.stdin = open('boj7785.txt')

T = int(input())

inout_dict = {}
result = []

for i in range(T):
    
    name, inout = input().split()

    if inout == 'enter':
        inout_dict[name] = 1
    else:
        inout_dict[name] = 0

result = list(inout_dict.keys())
result.sort(reverse=True)

for ii in range(len(result)):
    if inout_dict[result[ii]] == 1:
        print(result[ii])