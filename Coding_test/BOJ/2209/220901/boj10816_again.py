
T1 = int(input())
cards = list(map(int, input().split()))
cards_dict = {}

for i in cards:
    if i not in cards_dict:
        cards_dict[i] = 1
    else:
        cards_dict[i] += 1

T2 = int(input())
find_card = list(map(int, input().split()))

for ii in find_card:
    print(cards_dict.get(ii, 0), end = ' ')