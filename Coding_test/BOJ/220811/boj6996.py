T = int(input())

A_list = []
B_list = []

for _ in range(T):
    A, B = input().split()
    if len(A) != len(B):
        print(A,'&',B,'are NOT anagrams.')
        A_list = []
        B_list = []
        continue
    else:
        for i in range(len(A)):
            A_list.append(A[i])
            B_list.append(B[i])
    A_list.sort()
    B_list.sort()
    if A_list == B_list:
        print(A,'&',B,'are anagrams.')
        A_list = []
        B_list = []
    else:
        print(A,'&',B,'are NOT anagrams.')
        A_list = []
        B_list = []