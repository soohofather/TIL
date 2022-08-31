sentence = []
cnt = 0

while True:
    sentence = input()
    if sentence == '#':
        break
    for i in range(len(sentence)):
        if sentence[i] in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            cnt += 1
    print(cnt)
    cnt = 0