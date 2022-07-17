with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    
    fruits = f.read().split()

    dict = {}

    for findyou in fruits:
        dict[findyou] = dict.get(findyou, 0) + 1

    for a in dict:
        print(a, dict[a])

