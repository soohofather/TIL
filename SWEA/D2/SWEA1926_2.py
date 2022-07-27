n = int(input())
m = ''

for i in range(1, n + 1):
  i = str(i)
  for ii in i:
    if ii in ['3', '6', '9']:
      m += '-'
  if m == '':
    print(i, end=(' '))
  else:
    print(m, end=(' '))
    m = ''
