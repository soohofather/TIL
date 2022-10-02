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
counting.sorted()
print(counting)
