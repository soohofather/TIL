import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for i in range(T):
    
    card_numbers = str(input().split())
    new_numbers = ''

    for ii in card_numbers:
        if ii in ['\'', '[', ']', '-']:
            continue
        else:
            new_numbers += ii

    
    if new_numbers[0] not in ['3', '4', '5', '6', '9']:
        print(f'#{i+1}', 0)
    elif len(new_numbers) != 16:
        print(f'#{i+1}',0)
    else:
        print(f'#{i+1}',1)
