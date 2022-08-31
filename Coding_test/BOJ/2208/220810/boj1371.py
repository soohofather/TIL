import sys

sys.stdin = open('boj1371.txt')

dict_ = {}

while True:
    try:
        sentence = input()
    except EOFError:
        break
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            continue
        elif sentence[i] not in dict_:
            dict_[sentence[i]] = 0
        elif sentence[i] in dict_:
             dict_[sentence[i]] += 1

max_number = 0
key_ = []

for ii in dict_:
    if max_number <= dict_[ii]:
        max_number = dict_[ii]
else:
    for iii in dict_:
        if dict_[iii] == max_number:
            key_ += iii
key_.sort()

for iiii in key_:
    print(iiii, end=(''))