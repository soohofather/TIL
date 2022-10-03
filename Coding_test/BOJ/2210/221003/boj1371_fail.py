import sys

sys.stdin = open("test.txt")

counting = {}

while True:
    try:
        sentence = input()
        for i in range(len(sentence)):
            if sentence[i] == " ":
                continue
            else:
                if sentence[i] in counting:
                    counting[sentence[i]] += 1
                else:
                    counting[sentence[i]] = 1
    except EOFError:
        break

new_counting = sorted(counting.items(), key=lambda x: x[1], reverse=True)

result = ""

for ii in range(len(new_counting)):
    if ii == 0:
        result += new_counting[ii][0]
    else:
        if new_counting[ii][1] == new_counting[0][1]:
            result += new_counting[ii][0]
        else:
            break

new_result = sorted(result)

for iii in new_result:
    print(iii, end="")
