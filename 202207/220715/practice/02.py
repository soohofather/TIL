with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    fruits = f.read()
    new_fruits = set(fruits.split('\n'))

    cnt = 0
    ff = ''
    
    for f in new_fruits:
        if f[len(f) -5 : len(f)] == 'berry':
            cnt += 1
            ff += f + "\n"
    print(cnt)
    print(ff)
