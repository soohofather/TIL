a = [[],[],[],[],[]]
len_ = 0

for i in range(5):
    sentence = input()
    for ii in range(len(sentence)):
        a[i].append(sentence[ii])

for iiii in range(15):
    for iii in range(5):
        if len(a[iii]) == 0:
            continue
        c = a[iii].pop(0)
        print(c, end='')