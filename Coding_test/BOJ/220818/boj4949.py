while True:
    try:
        sentence = input()

        if sentence[0] == '.':
            break

        a = []
        b = []

        for i in range(len(sentence)):
            if sentence[i] == '(':
                a.append(sentence[i])
            elif sentence[i] == '[':
                a.append(sentence[i])
            elif sentence[i] == ')':
                if len(a) == 0:
                    print('no')
                    break
                else:
                    b = a.pop()
                    if b == '(':
                        b = []
                        continue
                    else:
                        print('no')
                        b = []
                        break
            elif sentence[i] == ']':
                if len(a) == 0:
                    print('no')
                    break
                else:
                    b = a.pop()
                    if b == '[':
                        b = []
                        continue
                    else:
                        print('no')
                        b = []
                        break
            elif sentence[i] == '.':
                if len(a) == 0:
                    print('yes')
                    a = []
                    b = []
                    break
                else:
                    print('no')
                    a = []
                    b = []
                    break
    except EOFError:
        break