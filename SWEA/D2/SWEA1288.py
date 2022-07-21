T = int(input())

for i in range(T):
  n = int(input())
  n = int(n)
  p = n
  m = 0
  o = []
  cnt = 0
  while o != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    n = p
    cnt += 1
    n *= cnt
    while n != 0:
      m = n % 10
      if m not in o:
            o.append(m)
      o = sorted(o)
      m = 0
      n //= 10
  print(f'#{i+1}', p*cnt)
