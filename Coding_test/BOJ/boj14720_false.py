T = int(input())
milk = list(map(int, input().split()))

status = []

for i in range(T):

    status_len = len(status)-1

    if status == []:
        if milk[i] == 0:
            status.append(milk[i])
        else:
            break
    else:
        if status[status_len] == 0:
            if milk[i] == 1:
                status.append(milk[i])
            else:
                break
        elif status[status_len] == 1:
            if milk[i] == 2:
                status.append(milk[i])
            else:
                break
        elif status[status_len] == 2:
            if milk[i] == 0:
                status.append(milk[i])
            else:
                break
print(len(status))
