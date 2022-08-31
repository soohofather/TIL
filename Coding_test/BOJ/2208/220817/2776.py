TC = int(input())

for _ in range(TC):
    
    a = int(input())
    suchup_1 = list(input().split())
    suchup_3 = set(suchup_1)
    b = int(input())
    suchup_2 = list(input().split())
    
    for i in suchup_2:
        print(1 if i in suchup_3 else 0)