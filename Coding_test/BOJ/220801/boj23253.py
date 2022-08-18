N, M = map(int, input().split())
true_false = True

for i in range(M):
    n = int(input())
    list_ = list(map(int, input().split()))
    if true_false:
        while len(list_) > 0:
            temp_list = list_.pop()
            if list_:
                if temp_list > list_[-1]:
                    true_false = False
                    break             
    else:
        break

print('yes' if true_false else 'No')