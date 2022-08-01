T = int(input())

for i in range(T):
    strings = '(()())((()))'
    finding = []
    for ii in strings:                      # '('가 들어오면 일단 추가. 괄호 열림
        if ii == '(':
            finding.append(ii)
        else:                               # ')'가 들어왓는데 기존에 '('가 없으면 뭔가 잘못 입력된 것이니 ) 추가하고 break
            if finding == []:
                finding.append(')')
                break
            else:                           # 기존에 '('가 있는 상태에서 '('가 들어온거면 1쌍이 해결되었으니 기존 '(' 없애기 단, )는 추가하지 않음
                finding.pop()
    print('YES' if finding ==[] else 'NO')  # 쌍쌍이 맞으면 하나도 남지 않을 것이고, 쌍이 안맞으면 )가 남아있을것임. 