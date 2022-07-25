star = int(input())

for i in range(star):
  if i % 2 == 0:
    print('* ' * star)
  elif i % 2 == 1:
    print(' *' * star)