T = int(input())
card = {}
for_cnt = 0

for i in range(T):
    number = int(input())
    if number not in card:
        card[number] = 1
    else:
        card[number] += 1
else:
    for_cnt = number

card_number = []
cnt = card[for_cnt]

for ii in card:
    if card[ii] > cnt:
        cnt = card[ii]
        card_number = [ii]
    elif card[ii] == cnt:
        card_number.append(ii)
card_number.sort()
print(card_number[0])