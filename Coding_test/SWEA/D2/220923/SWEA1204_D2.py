
TC = int(input())
for _ in range(TC):

    T = int(input())
    numbers = list(map (int, input().split()))
    number_dict = {}
    for i in numbers:
        if i in number_dict:
            number_dict[i] += 1
        else:
            number_dict[i] = 1

    sort_numbers = sorted(number_dict.items(), key = lambda x : x[1], reverse = True)
    print(f'#{T}', sort_numbers[0][0])

