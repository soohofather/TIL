nono = 'CAMBRIDGE'

mail = input()
result = ''

for i in range(len(mail)):
    if mail[i] in nono:
        continue
    else:
        result += mail[i]
print(result)