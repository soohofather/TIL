n = int(input())
m = ''

for i in range(1, n + 1):
    o = str(i)
    if len(o) == 1:
        if '3' in o or '6' in o or '9' in o:
            if o[0] == '3' or o[0] == '6' or o[0] == '9': 
                m += '-'
            print(m, end=(' '))
            m = ''        
        else:
            print(i, end=(' '))
    elif len(o) == 2:
        if '3' in o or '6' in o or '9' in o:
            if o[0] == '3' or o[0] == '6' or o[0] == '9': 
                m += '-'
            if o[1] == '3' or o[1] == '6' or o[1] == '9':
                m += '-'           
            print(m, end=(' '))
            m = ''
        else:
            print(i, end=(' '))
    elif len(o) == 3:
        if '3' in o or '6' in o or '9' in o:
            if o[0] == '3' or o[0] == '6' or o[0] == '9': 
                m += '-'
            if o[1] == '3' or o[1] == '6' or o[1] == '9':
                m += '-'
            if o[2] == '3' or o[2] == '6' or o[2] == '9':
                m += '-'
            print(m, end=(' '))
            m = ''
        else:
            print(i, end=(' '))