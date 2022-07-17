with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    
    cnt = 0
    for fruits in f:
        cnt += 1
    print(cnt)