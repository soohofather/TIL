while True:

    sentence = input()
    result = []
    if sentence == '.':
        break

    for i in sentence:
        if i == '(' or i == '[':
            result.append(i)
        elif i == ')':
            if len(result) == 0 :
                print('no')
                break
            else:
                check = result.pop()
                if check == '(':
                    check == []
                else:
                    print('no')
                    break
        elif i == ']':
            if len(result) == 0 :
                print('no')
                break
            else:
                check = result.pop()
                if check == '[':
                    check == []
                else:
                    print('no')
                    break
        elif i == '.':
            if len(result) == 0:
                print('yes')
                break
            else:
                print('no')
                break
