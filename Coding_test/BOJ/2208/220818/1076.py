ohm = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
gob = ''

gob += str(ohm.index(input()))
gob += str(ohm.index(input()))
gob += '0' * ohm.index(input())

print(int(gob))