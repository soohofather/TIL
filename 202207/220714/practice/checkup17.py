somoonja = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
daemoonja = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

fruit = input()
result = 0
char = ''

for findyou in fruit:
    for findyou2 in somoonja:
        if findyou == findyou2:
            char = char + daemoonja[result]
            result = 0
            break
        result += 1
print(char)
        
